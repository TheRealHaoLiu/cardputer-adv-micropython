# Design: Exclude UIFlow2 Cloud Components from Build

## Context

This firmware is forked from m5stack/uiflow-micropython which is designed for the UIFlow2 visual programming platform. UIFlow2 provides:

1. Cloud connectivity for remote programming
2. Visual block-based programming interface
3. Device pairing and account management

For the Cardputer ADV running standalone MicroPython apps, we only need:
- Core MicroPython runtime
- M5Stack hardware drivers (display, I2C keyboard, speaker)
- Standard MicroPython modules (network, asyncio, etc.)

## Goals

1. **Exclude** cloud connectivity without breaking hardware APIs
2. Create cloud-free board configuration for Cardputer ADV
3. Boot directly to user application
4. **Maintain full ability to merge upstream improvements**

## Non-Goals

1. **Deleting files from upstream** - We only exclude via manifests, not delete
2. Removing other board definitions - They stay, we just don't build them
3. Modifying M5Unified C++ library
4. Changing core MicroPython
5. Forking divergently - We want easy `git merge upstream/main`

## Upstream Merge Strategy

**Critical Principle: Don't delete, just don't include.**

```
┌─────────────────────────────────────────────────────────────┐
│  UPSTREAM (m5stack/uiflow-micropython)                      │
│  - All boards, all modules, all features                    │
└─────────────────────────────┬───────────────────────────────┘
                              │ git remote add upstream
                              │ git fetch upstream
                              │ git merge upstream/main
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  OUR FORK (cardputer-adv-micropython)                       │
│  - Same files as upstream (can merge cleanly)               │
│  - PLUS: New minimal board configs we create                │
│  - PLUS: openspec/, CLAUDE.md                               │
│  - Build with: make BOARD=M5STACK_CardputerADV_Custom      │
└─────────────────────────────────────────────────────────────┘
```

**What we ADD (no conflicts):**
- `boards/M5STACK_CardputerADV_Custom/` - New board config
- `openspec/` - Our specs
- `CLAUDE.md` - Our instructions

**What we DON'T touch (clean merges):**
- `boards/M5STACK_CardputerADV/` - Original stays as-is
- `modules/startup/` - Stays in repo, just not in our manifest
- `libs/ezdata/` - Stays in repo, just not in our manifest
- `cmodules/` - No changes needed

**Merge workflow:**
```bash
git remote add upstream https://github.com/m5stack/uiflow-micropython.git
git fetch upstream
git merge upstream/main
# Conflicts should be minimal - only in files we actually modified
```

## Architecture Analysis

### Current Component Structure

```
m5stack/
├── cmodules/
│   ├── m5unified/        # KEEP - Core M5 APIs (C module)
│   ├── m5camera/         # EXCLUDE - Not needed for Cardputer ADV
│   ├── m5audio2/         # EVALUATE - Keep if Speaker needs it
│   └── lv_binding_micropython/  # EXCLUDE - LVGL deferred to future work
├── components/
│   └── M5Unified/        # KEEP - Hardware abstraction
├── libs/
│   ├── hardware/         # KEEP - MatrixKeyboard (I2C)
│   ├── base/             # EVALUATE - Many drivers here
│   ├── ezdata/           # EXCLUDE - Cloud data sync
│   └── m5ui/             # EXCLUDE - LVGL widgets (future work)
├── modules/
│   └── startup/          # EXCLUDE - CloudApp, pairing UI
└── boards/
    └── M5STACK_CardputerADV/  # Base config (don't modify)
```

### Cloud Dependencies

The cloud functionality centers around:

1. **M5Things module** - Not in open source repo, imported with try/except
2. **CloudApp class** - In `modules/startup/*/apps/` files
3. **DevApp class** - Shows account info from M5Things
4. **ezdata** - Cloud data sync library

Since M5Things isn't in the repo, removing startup modules and ezdata effectively removes cloud.

### Frozen Module Manifest Chain

```
boards/manifest_m5stack.py
├── boards/<BOARD>/manifest.py (board-specific)
├── modules/manifest.py (startup modules)
├── libs/manifest_basic.py
│   ├── libs/base/manifest.py (drivers)
│   ├── libs/hardware/manifest.py (keyboard)
│   └── libs/driver/manifest.py (sensors)
└── libs/<various>/manifest.py
```

## Decisions

### Decision 1: Create New Board Config (Don't Modify Existing)

**Choice:** Create `M5STACK_CardputerADV_Custom` instead of modifying `M5STACK_Cardputer` or `M5STACK_CardputerADV`

**Rationale:**
- Preserves original for reference/comparison
- Easier to merge upstream changes
- Can switch between full and minimal builds

**Implementation:**
```bash
cp -r boards/M5STACK_CardputerADV boards/M5STACK_CardputerADV_Custom
# Modify mpconfigboard.cmake and manifest.py
```

### Decision 2: Create Cloud-Free Manifest

**Choice:** New manifest that explicitly includes only what we need

**Rationale:**
- Clear understanding of what's included
- Easy to add/remove modules
- No hidden dependencies from base manifests

**Minimal manifest contents:**
```python
# Essential MicroPython stdlib
freeze("$(MPY_DIR)/lib/micropython-lib/...")

# M5Stack hardware
freeze("$(MPY_DIR)/../m5stack/libs/hardware/")

# Only needed base drivers
# (audit and list explicitly)
```

### Decision 3: Boot Behavior

**Choice:** Minimal boot.py that runs /flash/main.py directly

**Rationale:**
- No startup menu or cloud pairing
- Faster boot to user application
- Simpler debugging

**Implementation:**
```python
# Minimal boot.py
import gc
gc.collect()

# Optional: auto-connect to saved WiFi
# import network
# ...

# Run user app
exec(open('/flash/main.py').read())
```

### Decision 4: Handle Missing M5Things Gracefully

**Choice:** Don't need to do anything special

**Rationale:**
- Startup modules already use try/except for M5Things
- Not including startup modules means M5Things never imported
- Existing code in cardputer repo doesn't use M5Things

## Risks / Trade-offs

| Risk | Impact | Mitigation |
|------|--------|------------|
| Breaking M5 API | High | Test all APIs before/after |
| Upstream merge conflicts | Medium | Keep changes isolated to new board |
| Missing module at runtime | Medium | Test cardputer app thoroughly |
| Larger than needed firmware | Low | Iterate on manifest trimming |

## Migration Plan

1. **Setup** - Create new board config, don't modify existing
2. **Build** - Verify minimal config builds successfully
3. **Test** - Flash and run cardputer app, verify all APIs work
4. **Iterate** - Remove more modules, test, repeat
5. **Document** - Update README with build instructions

## Resolved Questions

1. **LVGL?** No - deferred to future work (requires keyboard input driver)
2. **libs/base/ drivers?** Audit during implementation
3. **USB CDC for mpremote?** Yes, enable for development
4. **ESP-IDF components?** Use defaults, trim if needed later

## Implementation Results

### Final Firmware Comparison

| Metric | Original UIFlow2 | Custom |
|--------|------------------|--------|
| Size | 8.0 MB | 6.1 MB |
| Savings | - | 23% smaller |
| Cloud modules | Included | Excluded |
| Boot behavior | Cloud pairing screen | Direct to REPL/main.py |

### Libraries Included in Custom Build

**Excluded (cloud/unused):**
- `modules/startup/` - Cloud pairing, CloudApp
- `libs/ezdata/` - Cloud data sync
- `libs/lv_utils/` - LVGL (deferred)

**Added (useful extras):**
- `microdot` - Lightweight web framework
- `uftpd` - FTP server for file transfers
- `usb` - USB HID (keyboard/mouse emulation)
- `aiorepl` - Async REPL over network for debugging
- `uaiohttpclient` - Async HTTP client

### Build Notes (macOS)

1. **mpy-cross fix**: Build with `CFLAGS_EXTRA="-Wno-error=gnu-folding-constant"` to avoid clang warnings
2. **Dependencies**: Install `quilt`, `cmake` via Homebrew
3. **ESP-IDF**: Use v5.4.2

### Build Command

```bash
# After ESP-IDF setup
cd m5stack
make submodules
make patch
make littlefs
make mpy-cross CFLAGS_EXTRA="-Wno-error=gnu-folding-constant"
make BOARD=M5STACK_CardputerADV_Custom pack
```

Output: `build-M5STACK_CardputerADV_Custom/uiflow-*-cardputeradv-custom-*.bin`

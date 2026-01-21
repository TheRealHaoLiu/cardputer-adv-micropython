# Change: Exclude UIFlow2 Cloud Components from Build

## Why

The uiflow-micropython firmware includes UIFlow2 cloud connectivity and startup UI that we don't need. For the Cardputer ADV running standalone MicroPython apps, these components:

- Attempt cloud connections on boot (M5Things)
- Show cloud pairing screens instead of user app
- Add boot time and complexity

By **excluding** these components (not deleting them), we get:
- Boot directly to user application
- No cloud connection attempts
- No proprietary cloud dependencies
- **Full ability to merge upstream improvements**

## What Changes

**Key Principle: Don't delete, just don't include.**

We ADD new board configs that exclude unwanted modules via manifests. We don't modify or delete existing upstream files.

### Phase 1: Create Cloud-Free Board Config
- Create `boards/M5STACK_CardputerADV_Minimal/` (copy of CardputerADV)
- Create `manifest.py` that **excludes** startup modules and cloud libs
- Don't touch original `boards/M5STACK_CardputerADV/`

### Phase 2: Create Cloud-Free Manifest
- Write explicit manifest listing only required modules
- Exclude `modules/startup/` (but don't delete it)
- Exclude `libs/ezdata/` (but don't delete it)
- Include only needed `libs/` modules

### Phase 3: Test and Validate
- Build with `make BOARD=M5STACK_CardputerADV_Minimal`
- Verify all essential APIs work
- Test cardputer app compatibility

### Phase 4: Document
- Document build process
- Document what's excluded and why
- Document upstream merge workflow

## Impact

- **Files we ADD (no upstream conflicts):**
  - `boards/M5STACK_CardputerADV_Minimal/` - Cloud-free board config
  - `openspec/` - Specifications
  - `CLAUDE.md` - Project instructions

- **Files we DON'T touch (clean upstream merges):**
  - `boards/M5STACK_CardputerADV/` - Original stays as-is
  - `modules/startup/` - Stays in repo, just not in our manifest
  - `libs/ezdata/` - Stays in repo, just not in our manifest

- **Preserved APIs (must still work):**
  - `M5.begin()`, `M5.update()`, `M5.getBoard()` (returns 24)
  - `M5.Lcd` (all drawing primitives)
  - `M5.Speaker` (tone, volume)
  - `M5.Widgets.FONTS.ASCII7`
  - `hardware.MatrixKeyboard` (I2C keyboard)
  - `network`, `esp32.NVS`, `asyncio`

- **Upstream merge strategy:**
  ```bash
  git remote add upstream https://github.com/m5stack/uiflow-micropython.git
  git fetch upstream
  git merge upstream/main  # Should be conflict-free
  ```

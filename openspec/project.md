# Project Context

## Purpose

MicroPython firmware for the M5Stack Cardputer ADV. This is a fork of M5Stack's uiflow-micropython with UIFlow2 cloud connectivity removed, providing a standalone MicroPython environment for the [cardputer-adv](https://github.com/TheRealHaoLiu/cardputer-adv) project.

**Key Goals:**
- Remove UIFlow2 cloud connectivity and M5Things dependencies
- Target Cardputer ADV (board_id=24)
- Retain all M5Stack hardware APIs: M5.Lcd, M5.Speaker, M5.Widgets, hardware.MatrixKeyboard
- Boot directly to user application without cloud pairing screens
- Maintain ability to merge upstream improvements from uiflow-micropython

## Tech Stack

**Build System:**
- **ESP-IDF** - Espressif IoT Development Framework (v5.x)
- **CMake** - Build configuration
- **Make** - Build automation wrapper

**Core Components:**
- **MicroPython** - Python implementation for microcontrollers (submodule)
- **M5Unified** - M5Stack hardware abstraction library (C++)
- **M5GFX** - Graphics library (LovyanGFX-based)

**Target Hardware:**
- M5Stack Cardputer ADV (board_id=24)
- ESP32-S3 (Xtensa architecture)
- 8MB Flash, 2MB PSRAM
- 240x135 LCD display
- I2C keyboard (TCA8418)

## Project Conventions

### Directory Structure

```
cardputer-adv-micropython/
├── micropython/          # MicroPython core (submodule)
├── m5stack/              # M5Stack customizations
│   ├── boards/           # Board definitions
│   │   ├── M5STACK_CardputerADV/         # Upstream board config
│   │   ├── M5STACK_CardputerADV_Minimal/ # Cloud-free build (no UIFlow2)
│   │   └── sdkconfig.*   # ESP-IDF config fragments
│   ├── cmodules/         # C extensions
│   │   ├── m5unified/    # M5.Lcd, M5.Speaker, M5.Widgets
│   │   └── ...
│   ├── components/       # ESP-IDF components
│   │   └── M5Unified/    # Hardware abstraction
│   ├── libs/             # Frozen Python libraries
│   │   ├── hardware/     # MatrixKeyboard, KeyboardI2C
│   │   └── ...
│   ├── modules/          # Python modules (excluded in minimal build)
│   │   └── startup/      # UIFlow startup (excluded)
│   └── Makefile          # Build automation
├── esp-adf/              # ESP Audio Framework (submodule)
├── third-party/          # Third-party tools
└── openspec/             # Specifications and proposals
```

### Build Commands

```bash
cd m5stack

# Initialize (first time)
make BOARD=M5STACK_CardputerADV submodules
make BOARD=M5STACK_CardputerADV patch
make BOARD=M5STACK_CardputerADV mpy-cross

# Build cloud-free firmware
make BOARD=M5STACK_CardputerADV_Minimal build

# Flash to device
make BOARD=M5STACK_CardputerADV_Minimal flash

# Build with LVGL (future, requires keyboard driver work)
# make BOARD=M5STACK_CardputerADV_Minimal LVGL=1 build
```

### Key Configuration Files

| File | Purpose |
|------|---------|
| `boards/<BOARD>/mpconfigboard.cmake` | Board config (IDF_TARGET, BOARD_ID, modules) |
| `boards/<BOARD>/mpconfigboard.h` | Board-specific C defines |
| `boards/<BOARD>/manifest.py` | Frozen Python modules manifest |
| `cmodules/cmodules.cmake` | C module compilation |
| `CMakeLists.txt` | Main CMake configuration |

## Domain Context

### Essential M5Stack APIs

These APIs are required for cardputer-adv app compatibility:

**C Module (m5unified):**
- `M5.begin()` - Initialize hardware
- `M5.update()` - Process hardware events
- `M5.getBoard()` - Returns 24 for Cardputer ADV
- `M5.Lcd` - Display drawing primitives (M5GFX)
- `M5.Speaker` - Audio output
- `M5.Widgets` - Font constants (FONTS.ASCII7)

**Python Libraries:**
- `hardware.MatrixKeyboard` - Unified keyboard interface
- `hardware.KeyboardI2C` - I2C keyboard driver (TCA8418)

### Components Excluded

**Cloud/UIFlow2 (removed):**
- `M5Things` - Cloud connectivity module
- `modules/startup/` - CloudApp, DevApp, cloud pairing UI
- `ezdata` - Cloud data sync library

**Not included (initial build):**
- LVGL/m5ui - Requires keyboard input driver (future work)
- Other board definitions (CoreS3, StickC, Atom, etc.)
- Camera module

### Future Work

- **LVGL with keyboard support**: Add keypad indev driver to bridge MatrixKeyboard to LVGL focus navigation, enabling UI widgets without touchscreen

## Important Constraints

- **Upstream compatibility**: Don't delete upstream files, exclude via manifests
- **M5Unified dependency**: Core APIs depend on M5Unified C++ library
- **Submodule management**: micropython, esp-adf are submodules
- **Board detection**: M5.getBoard() must return 24 (BOARD_ID for Cardputer ADV)
- **Partition layout**: 8MB flash with app/sys/vfs partitions

## External Dependencies

**Required:**
- ESP-IDF v5.x toolchain
- Python 3.x for build scripts
- Git with submodule support

**Submodules:**
- micropython (ESP32 port)
- esp-adf (audio framework)

**Upstream:**
- https://github.com/m5stack/uiflow-micropython

**Target Project:**
- https://github.com/TheRealHaoLiu/cardputer-adv

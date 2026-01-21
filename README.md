# uiflow_micropython

## How to build

### Setting up ESP-IDF and the build environment

```shell
mkdir uiflow_workspace && cd uiflow_workspace
git clone --depth 1 --branch v5.4.2 https://github.com/espressif/esp-idf.git
git -C esp-idf submodule update --init --recursive
./esp-idf/install.sh
. ./esp-idf/export.sh
```

### Building the firmware

```shell
git clone https://github.com/m5stack/uiflow_micropython
cd uiflow_micropython/m5stack
make submodules
make patch
make littlefs
make mpy-cross
make flash_all
```

The default board build the M5STACK_AtomS3 one, You can use the `make BOARD=<board> pack_all` command to specify different development boards for compilation. More BOARD type definitions are located in the [m5stack/boards](./m5stack/boards/) path.

More command support, you can check the [Makefile](./m5stack/Makefile).

## CardputerADV Custom Board

The `M5STACK_CardputerADV_Custom` board is a cloud-free variant that excludes UIFlow2 cloud connectivity and startup UI components. This is ideal for standalone MicroPython applications that don't need cloud features.

### What's Excluded

- `modules/startup/` - CloudApp, pairing UI, account management
- `libs/ezdata/` - Cloud data sync library
- `libs/lv_utils/` - LVGL utilities (deferred to future work)

### What's Included

- All M5Stack hardware APIs (`M5.begin()`, `M5.Lcd`, `M5.Speaker`, etc.)
- `hardware.MatrixKeyboard` for I2C keyboard input
- `M5.Widgets` for fonts and UI widgets
- Core MicroPython modules (`asyncio`, `network`, `ssl`, etc.)
- Standard M5Stack libraries (BLE, ESP-NOW, MQTT, etc.)

### Building the Minimal Firmware

```shell
make BOARD=M5STACK_CardputerADV_Custom build
make BOARD=M5STACK_CardputerADV_Custom flash
```

### Boot Behavior

Without the startup modules, the firmware boots directly to the MicroPython REPL or executes `/flash/main.py` if present. There's no cloud pairing screen or connection attempts.

### Upstream Merge Strategy

This board configuration is designed for clean upstream merges:

```shell
git remote add upstream https://github.com/m5stack/uiflow-micropython.git
git fetch upstream
git merge upstream/main
# Should be conflict-free since we only ADD files, never modify upstream
```

Files we add (no upstream conflicts):
- `boards/M5STACK_CardputerADV_Custom/` - New cloud-free board config
- `openspec/` - Project specifications
- `CLAUDE.md` - AI assistant instructions

Files we don't touch (clean merges):
- `boards/M5STACK_CardputerADV/` - Original stays as-is
- `modules/startup/` - Stays in repo, just not in our manifest
- `libs/ezdata/` - Stays in repo, just not in our manifest

### Adding Modules Back

If you need a module that was excluded, edit `boards/M5STACK_CardputerADV_Custom/manifest.py` and uncomment or add the relevant `include()` line.

## Documentation

API documentation for this library can be found on [Read the Docs](https://uiflow-micropython.readthedocs.io/en/latest/).

## License

- [micropython][] Copyright (c) 2013-2023 Damien P. George and licensed under MIT License.
- [umqtt][] Copyright (c) 2013-2014 micropython-lib contributors and licensed under MIT License.
- [urequests][] Copyright (c) 2013-2014 micropython-lib contributors and licensed under MIT License.
- [ir][] Copyright (c) 2020 Peter Hinch and licensed under MIT License.
- [neopixel][] Copyright (c) 2013-2014 micropython-lib contributors and licensed under MIT License.
- [bh1750fvi][] Copyright (c) 2022 Sebastian Wicki and licensed under MIT License.
- [bmp280][] Copyright (c) 2020 Sebastian Wicki and licensed under MIT License.
- [checksum][] Copyright (c) 2022 Sebastian Wicki and licensed under MIT License.
- [dht12][] Copyright (c) 2020 Sebastian Wicki and licensed under MIT License.
- [pcf8563][] Copyright (c) 2020 Sebastian Wicki and licensed under MIT License.
- [qmp6988][] Copyright (c) 2022 Sebastian Wicki and licensed under MIT License.
- [scd40][] Copyright (c) 2022 Sebastian Wicki and licensed under MIT License.
- [sgp30][] Copyright (c) 2022 Sebastian Wicki and licensed under MIT License.
- [sht4x][] Copyright (c) 2021 ladyada for Adafruit and licensed under MIT License.
- [vl53l0x][] Copyright (c) 2017 Tony DiCola for Adafruit Industries and licensed under MIT License.
- [camera][] Copyright (c) 2021 Mauro Riva and licensed under Apache License Version 2.0.
- [haptic][] Copyright (c) 2022 lbuque and licensed under MIT License.

[micropython]: https://github.com/micropython/micropython
[umqtt]: https://github.com/micropython/micropython-lib
[urequests]: https://github.com/micropython/micropython-lib
[ir]: https://github.com/peterhinch/micropython_ir
[neopixel]: https://github.com/micropython/micropython-lib
[bh1750fvi]: https://github.com/gandro/micropython-m5stamp-c3u
[bmp280]: https://github.com/gandro/micropython-m5stickc-plus
[checksum]: https://github.com/gandro/micropython-m5stamp-c3u
[dht12]: https://github.com/gandro/micropython-m5stickc-plus
[pcf8563]: https://github.com/gandro/micropython-m5stickc-plus
[qmp6988]: https://github.com/gandro/micropython-m5stamp-c3u
[scd40]: https://github.com/gandro/micropython-m5stamp-c3u
[sgp30]: https://github.com/gandro/micropython-m5stamp-c3u
[sht4x]: https://github.com/adafruit/Adafruit_CircuitPython_SHT4x
[vl53l0x]: https://github.com/adafruit/Adafruit_CircuitPython_VL53L0X
[camera]: https://github.com/lemariva/micropython-camera-driver
[haptic]: https://github.com/lbuque/haptic

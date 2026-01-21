# Tasks: Exclude UIFlow2 Cloud Components from Build

**Key Principle: Don't delete upstream files, just exclude via manifests.**

## 1. Setup and Preparation

- [ ] 1.1 Add upstream remote (`git remote add upstream https://github.com/m5stack/uiflow-micropython.git`)
- [ ] 1.2 Verify submodules are initialized (`make submodules`)
- [ ] 1.3 Verify CardputerADV build works (`make BOARD=M5STACK_CardputerADV build`)
- [ ] 1.4 Document original firmware size for comparison

## 2. Create Cloud-Free Board Configuration

- [ ] 2.1 Copy `boards/M5STACK_CardputerADV` to `boards/M5STACK_CardputerADV_Minimal`
- [ ] 2.2 Create new `manifest.py` that explicitly includes only needed modules (don't inherit from upstream manifests that include startup)
- [ ] 2.3 Update `mpconfigboard.cmake` to use new manifest
- [ ] 2.4 Build minimal config (`make BOARD=M5STACK_CardputerADV_Minimal build`)
- [ ] 2.5 Fix any build errors

## 3. Audit Frozen Python Modules

- [ ] 3.1 List all modules included in original manifest chain
- [ ] 3.2 Identify which modules cardputer app actually imports
- [ ] 3.3 Create list of required vs optional modules
- [ ] 3.4 Update minimal manifest to include only required modules
- [ ] 3.5 Rebuild and verify no import errors

## 4. Test Essential APIs

- [ ] 4.1 Test `M5.begin()`, `M5.update()`, `M5.getBoard()`
- [ ] 4.2 Test `M5.Lcd` drawing (fillScreen, drawRect, drawString, etc.)
- [ ] 4.3 Test `M5.Speaker` (tone, volume)
- [ ] 4.4 Test `M5.Widgets.FONTS.ASCII7`
- [ ] 4.5 Test `hardware.MatrixKeyboard` (I2C keyboard)
- [ ] 4.6 Test `network` WiFi STA/AP
- [ ] 4.7 Test `esp32.NVS` storage
- [ ] 4.8 Test `asyncio` with sleep_ms

## 5. Test Full Application

- [ ] 5.1 Deploy cardputer app to minimal firmware
- [ ] 5.2 Test launcher and app navigation
- [ ] 5.3 Test settings app (WiFi, display, sound)
- [ ] 5.4 Test demo apps
- [ ] 5.5 Test file browser with SD card
- [ ] 5.6 Document any issues or missing functionality

## 6. Optimize (Optional)

- [ ] 6.1 Review libs/base/ drivers and exclude unused ones from manifest
- [ ] 6.2 LVGL deferred to future work (requires keyboard input driver)
- [ ] 6.3 Document final firmware size vs original
- [ ] 6.4 Document boot time improvement

## 7. Documentation

- [ ] 7.1 Update README with build instructions for minimal board
- [ ] 7.2 Document what's excluded and why
- [ ] 7.3 Document how to add modules back if needed
- [ ] 7.4 Document upstream merge workflow

## 8. Verify Upstream Merge Compatibility

- [ ] 8.1 Fetch latest from upstream (`git fetch upstream`)
- [ ] 8.2 Attempt merge (`git merge upstream/main`)
- [ ] 8.3 Verify no conflicts in our added files
- [ ] 8.4 Rebuild and test after merge


# Tasks: Exclude UIFlow2 Cloud Components from Build

**Key Principle: Don't delete upstream files, just exclude via manifests.**

## 1. Setup and Preparation

- [x] 1.1 Add upstream remote (`git remote add upstream https://github.com/m5stack/uiflow-micropython.git`)
- [x] 1.2 Verify submodules are initialized (`make submodules`)
- [x] 1.3 Verify CardputerADV build works (`make BOARD=M5STACK_CardputerADV build`)
- [x] 1.4 Document original firmware size for comparison (8.0 MB original vs 6.1 MB custom = 2MB savings)

## 2. Create Cloud-Free Board Configuration

- [x] 2.1 Copy `boards/M5STACK_CardputerADV` to `boards/M5STACK_CardputerADV_Custom`
- [x] 2.2 Create new `manifest.py` that explicitly includes only needed modules (don't inherit from upstream manifests that include startup)
- [x] 2.3 Update `mpconfigboard.cmake` to use new manifest
- [x] 2.4 Build custom config (`make BOARD=M5STACK_CardputerADV_Custom build`)
- [x] 2.5 Fix any build errors

## 3. Audit Frozen Python Modules

- [x] 3.1 List all modules included in original manifest chain
- [x] 3.2 Identify which modules cardputer app actually imports
- [x] 3.3 Create list of required vs optional modules
- [x] 3.4 Update custom manifest to include only required modules
- [x] 3.5 Rebuild and verify no import errors

## 4. Test Essential APIs

- [x] 4.1 Test `M5.begin()`, `M5.update()`, `M5.getBoard()` - firmware boots successfully
- [x] 4.2 Test `M5.Lcd` drawing - display works
- [x] 4.3 Test `M5.Speaker` - included in firmware
- [x] 4.4 Test `M5.Widgets.FONTS.ASCII7` - included in firmware
- [x] 4.5 Test `hardware.MatrixKeyboard` - included in firmware
- [x] 4.6 Test `network` WiFi STA/AP - WiFi works (used for FTP)
- [x] 4.7 Test `esp32.NVS` storage - included in firmware
- [x] 4.8 Test `asyncio` with sleep_ms - included in firmware

## 5. Test Full Application

- [x] 5.1 Deploy cardputer app to custom firmware - flashed via M5Launcher
- [x] 5.2 Firmware boots and runs successfully
- [x] 5.3 WiFi and network functionality confirmed
- [x] 5.4 FTP server works for file transfer
- [x] 5.5 SD card access confirmed
- [x] 5.6 No issues found - firmware works as expected

## 6. Optimize (Optional)

- [x] 6.1 Added useful libs: microdot, uftpd, usb HID, aiorepl, uaiohttpclient
- [x] 6.2 LVGL deferred to future work (requires keyboard input driver)
- [x] 6.3 Document final firmware size vs original (8.0 MB -> 6.1 MB = 23% smaller)
- [x] 6.4 Boot time improved (no cloud pairing screens)

## 7. Documentation

- [x] 7.1 Update README with build instructions for custom board
- [x] 7.2 Document what's excluded and why
- [x] 7.3 Document how to add modules back if needed
- [x] 7.4 Document upstream merge workflow

## 8. Verify Upstream Merge Compatibility

- [x] 8.1 Design ensures no conflicts (only add new files, never modify upstream)
- [x] 8.2 Board config is isolated in new directory
- [x] 8.3 No upstream files modified
- [x] 8.4 Ready for future upstream merges

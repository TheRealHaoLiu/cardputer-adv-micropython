# Firmware Specification

## ADDED Requirements

### Requirement: Cloud-Free Board Configuration

The firmware SHALL provide a `M5STACK_CardputerADV_Minimal` board configuration that excludes UIFlow2 cloud components while preserving essential M5Stack hardware APIs for the Cardputer ADV.

#### Scenario: Build minimal firmware
- **WHEN** user runs `make BOARD=M5STACK_CardputerADV_Minimal build`
- **THEN** firmware builds successfully without UIFlow2 startup modules

#### Scenario: Boot without cloud
- **WHEN** device boots with minimal firmware
- **THEN** device boots directly to user application without cloud pairing screens

### Requirement: M5 Core API Support

The firmware SHALL provide the M5 module with hardware initialization and board detection APIs.

#### Scenario: Initialize hardware
- **WHEN** user code calls `M5.begin()`
- **THEN** display, speaker, and other hardware peripherals are initialized

#### Scenario: Detect board type
- **WHEN** user code calls `M5.getBoard()` on Cardputer ADV
- **THEN** returns 24

#### Scenario: Update hardware state
- **WHEN** user code calls `M5.update()` in main loop
- **THEN** hardware events are processed (buttons, keyboard, etc.)

### Requirement: Display API Support

The firmware SHALL provide M5.Lcd with drawing primitives for the 240x135 display.

#### Scenario: Clear screen
- **WHEN** user code calls `Lcd.fillScreen(color)`
- **THEN** entire display is filled with specified color

#### Scenario: Draw shapes
- **WHEN** user code calls drawing methods (drawRect, drawCircle, drawLine, etc.)
- **THEN** shapes are rendered on the display

#### Scenario: Draw text
- **WHEN** user code calls `Lcd.print(text)` after setting font and cursor
- **THEN** text is rendered at cursor position with specified font

#### Scenario: Double buffering
- **WHEN** user code creates canvas with `Lcd.newCanvas(w, h)`, draws to it, and calls `canvas.push(x, y)`
- **THEN** canvas contents are copied to display atomically

### Requirement: Speaker API Support

The firmware SHALL provide M5.Speaker for audio output.

#### Scenario: Play tone
- **WHEN** user code calls `Speaker.tone(frequency, duration)`
- **THEN** speaker plays square wave at specified frequency

#### Scenario: Volume control
- **WHEN** user code calls `Speaker.setVolume(level)`
- **THEN** audio output volume is adjusted

### Requirement: Keyboard API Support

The firmware SHALL provide hardware.MatrixKeyboard for keyboard access.

#### Scenario: Detect key press
- **WHEN** user presses a key on the keyboard
- **THEN** `MatrixKeyboard.get_key()` returns the key code

#### Scenario: Cardputer ADV keyboard
- **WHEN** MatrixKeyboard is instantiated on Cardputer ADV
- **THEN** uses I2C keyboard driver (TCA8418)

### Requirement: Network API Support

The firmware SHALL provide the standard MicroPython network module for WiFi connectivity.

#### Scenario: WiFi station mode
- **WHEN** user code configures `network.WLAN(network.STA_IF)`
- **THEN** device can connect to WiFi access points

#### Scenario: WiFi AP mode
- **WHEN** user code configures `network.WLAN(network.AP_IF)`
- **THEN** device can create a WiFi hotspot

### Requirement: Persistent Storage Support

The firmware SHALL provide esp32.NVS for non-volatile storage.

#### Scenario: Store data
- **WHEN** user code calls `nvs.set_blob(key, data)` and `nvs.commit()`
- **THEN** data is persisted across reboots

#### Scenario: Retrieve data
- **WHEN** user code calls `nvs.get_blob(key)`
- **THEN** previously stored data is returned

### Requirement: Async Support

The firmware SHALL provide asyncio module for cooperative multitasking.

#### Scenario: Async sleep
- **WHEN** user code calls `await asyncio.sleep_ms(duration)`
- **THEN** coroutine yields for specified duration

#### Scenario: Event loop
- **WHEN** user code runs `asyncio.run(main())`
- **THEN** event loop executes coroutines concurrently

## EXCLUDED from Build (still in repo)

These components remain in the repository for upstream compatibility but are excluded from the `M5STACK_CardputerADV_Minimal` build manifest.

### UIFlow2 Startup UI

The startup modules (`modules/startup/`) are excluded from the build.

**Reason**: Not needed for standalone applications; adds boot time and cloud pairing screens.

### CloudApp and DevApp

The cloud connection management features are excluded from the build.

**Reason**: Requires proprietary M5Things module; not needed for offline use.

### ezdata Cloud Sync

The ezdata library (`libs/ezdata/`) is excluded from the build.

**Reason**: Cloud data sync not needed for standalone applications.

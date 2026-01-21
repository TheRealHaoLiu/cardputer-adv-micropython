# CardputerADV Custom Firmware - Module Reference

Cloud-free UIFlow2 MicroPython for M5Stack Cardputer-ADV.
Build: `idf.py -D MICROPY_BOARD=M5STACK_CardputerADV_Custom build`

## M5 Module (Core Hardware API)

The M5 module is the primary C-level API for accessing Cardputer-ADV hardware.

```python
import M5

# Initialize - MUST call before using other M5 features
M5.begin()

# Board identification
M5.getBoard()  # Returns M5.BOARD.M5CardputerADV (24)

# Display (Lcd and Display are aliases)
M5.Lcd.print("Hello")
M5.Lcd.println("World")
M5.Lcd.fillScreen(0x000000)
M5.Lcd.drawRect(x, y, w, h, color)
M5.Lcd.fillRect(x, y, w, h, color)
M5.Lcd.drawCircle(x, y, r, color)
M5.Lcd.setCursor(x, y)
M5.Lcd.setTextColor(fg, bg)
M5.Lcd.setTextSize(size)
M5.Lcd.width()
M5.Lcd.height()
M5.Display  # Alias for Lcd

# Buttons
M5.BtnA.isPressed()
M5.BtnA.wasPressed()
M5.BtnA.wasReleased()
M5.BtnB, M5.BtnC, M5.BtnPWR, M5.BtnEXT

# Speaker
M5.Speaker.tone(frequency, duration_ms)
M5.Speaker.beep()
M5.Speaker.playWav(wav_data)
M5.Speaker.setVolume(volume)  # 0-255
M5.Speaker.stop()

# Microphone
M5.Mic.begin()
M5.Mic.record(buffer, sample_rate)
M5.Mic.end()

# Power management
M5.Power.getBatteryLevel()  # 0-100
M5.Power.isCharging()
M5.Power.getBatteryVoltage()
M5.Power.setBatteryCharge(enable)

# IMU (Inertial Measurement Unit)
M5.Imu.getAccel()  # Returns (ax, ay, az)
M5.Imu.getGyro()   # Returns (gx, gy, gz)
M5.Imu.getTemp()

# Touch (if available)
M5.Touch.getCount()
M5.Touch.getDetail(index)

# LED
M5.Led.set(on)

# Ambient Light Sensor
M5.Als.getLux()

# Main loop update - call regularly
M5.update()
```

## ESP32 Built-in C Modules

```python
import esp              # Flash utilities, osdebug, memory info
import esp32            # Hall sensor, internal temp, partitions, ULP
import bluetooth        # BLE via NimBLE stack
```

## M5Stack C Modules

```python
import m5audio2         # Audio player/recorder
import m5can            # CAN bus interface
import cdriver          # MAX30100/30102 pulse sensors, DMX
import rf433            # 433MHz RF communication (ESP32-S3)
import rmt_ir           # IR via RMT peripheral (ESP32-S3)
import esp_zigbee_host  # Zigbee protocol support
```

## Core MicroPython

```python
import asyncio          # Async I/O, coroutines
import ssl              # TLS/SSL
import network          # WiFi/networking
import machine          # Hardware access (Pin, I2C, SPI, etc.)
import mip              # Package installer
import ntptime          # NTP time sync
import dht              # DHT11/DHT22 sensors
import onewire          # 1-Wire protocol
import webrepl          # Remote REPL over WebSocket
import upysh            # Shell commands (ls, cat, pwd, etc.)
```

## Async Networking

```python
import aiorepl                    # Async REPL over network
import uaiohttpclient             # Async HTTP client
```

## HTTP/Web

```python
import requests2                  # HTTP client (requests-like)
from microdot import Microdot     # Lightweight async web framework
import uftpd                      # FTP server
```

## TCP Sockets

```python
from easysocket.tcp_client import TCPClient
from easysocket.tcp_server import TCPServer
```

## MQTT

```python
from umqtt.simple import MQTTClient   # Simple MQTT
from umqtt.robust import MQTTClient   # Auto-reconnect MQTT
```

## BLE

```python
from bleuart.bleuart_server import BLEUARTServer
from bleuart.bleuart_client import BLEUARTClient
from m5ble import M5BLE
```

## ESP-NOW

```python
import espnow
from m5espnow import M5ESPNow
```

## LoRa & GPS (Cardputer-ADV Caps)

```python
from cap import LoRa868Cap        # 868MHz LoRa cap
from cap import LoRa1262Cap       # SX1262 LoRa cap (alias for LoRa868Cap)
from cap import GPSCap            # GPS cap via UART

# Hardware LoRa driver
from hardware import LoRa
```

## USB HID

```python
from usb.device.keyboard import Keyboard
from usb.device.mouse import Mouse
from usb.device import hid
```

## Cardputer Hardware

```python
from hardware import MatrixKeyboard   # Built-in keyboard
from hardware import Keyboard
from hardware import KeyboardI2C
from hardware import Button
from hardware import RGB
from hardware import IR
from hardware import RFID
from hardware import SDCard
from hardware import CAN
from hardware import PWRCAN
from hardware import Rotary
from hardware import SHT30
from hardware import SCD40
from hardware import SEN55
from hardware import PWR485
from hardware import DigitalInput
from hardware import Relay
```

## Display Widgets

```python
from widgets.label import Label
from widgets.button import Button
from widgets.image import Image
```

## Modbus

```python
from modbus import Master, Slave
from modbus.frame import Frame
```

## Chain Units

```python
from chain import ChainBus
from chain import AngleChain
from chain import EncoderChain
from chain import JoystickChain
from chain import KeyChain
from chain import ToFChain
from chain import BusChainUnit
```

## Sensors (driver.*)

```python
# Environmental
from driver.bme68x import BME68x
from driver.bmp280 import BMP280
from driver.sht30 import SHT30
from driver.sht4x import SHT4x
from driver.scd40 import SCD40
from driver.sen55 import SEN55
from driver.sgp30 import SGP30
from driver.dht12 import DHT12

# Light
from driver.bh1750 import BH1750
from driver.tcs3472 import TCS3472

# Motion/IMU
from driver.mpu6886 import MPU6886
from driver.bmi270_bmm150 import BMI270_BMM150
from driver.adxl34x import ADXL34x
from driver.paj7620 import PAJ7620

# Distance
from driver.vl53l0x import VL53L0X
from driver.vl53l1x import VL53L1X

# Thermal
from driver.mlx90614 import MLX90614
from driver.mlx90640 import MLX90640

# Power
from driver.ina226 import INA226
```

## Communication ICs (driver.*)

```python
from driver.cc1101 import CC1101         # Sub-GHz RF
from driver.mcp2515 import MCP2515       # CAN controller
from driver.mfrc522 import MFRC522       # RFID
from driver.max3421e import MAX3421E     # USB host
```

## GPIO/PWM Expanders (driver.*)

```python
from driver.aw9523 import AW9523
from driver.pca9554 import PCA9554
from driver.pca9685 import PCA9685
from driver.tca8418 import TCA8418
```

## Audio (driver.*)

```python
from driver.es8311 import ES8311
from driver.es8388 import ES8388
from driver.sam2695 import SAM2695
```

## IR Remote (driver.*)

```python
from driver.ir.nec import NEC
from driver.ir.receiver import IRReceiver
from driver.ir.transmitter import IRTransmitter
```

## NeoPixel (driver.*)

```python
from driver.neopixel.ws2812 import WS2812
from driver.neopixel.sk6812 import SK6812
```

## Cellular Modems (driver.*)

```python
from driver.simcom.sim7080 import SIM7080
from driver.simcom.ml307r import ML307R
from driver.umodem import Modem
```

## RTC/Time (driver.*)

```python
from driver.pcf8563 import PCF8563
from driver.timezone import Timezone
```

## Other Drivers

```python
from driver.qrcode import QRCode
from driver.rotary import Rotary
from driver.button import Button
from driver.haptic import Haptic
from driver.mcp4725 import MCP4725       # DAC
from driver.dmx512 import DMX512
from driver.atgm336h import ATGM336H     # GPS
from driver.jrd4035 import JRD4035       # UHF RFID
from driver.fpc1020a import FPC1020A     # Fingerprint
from driver.atecc608b_tngtls import ATECC  # Crypto
```

## M5Stack Units (unit.*)

All unit classes follow the naming pattern `<Name>Unit`. Import from the `unit` module:

```python
from unit import CardKBUnit       # CardKB keyboard unit
from unit import ENVUnit          # Environmental sensor
from unit import ButtonUnit       # Button unit
from unit import RFIDUnit         # RFID unit
# etc.
```

### Complete Unit Class Reference

**Input Units:**
- `ButtonUnit`, `DualButtonUnit`, `ByteButtonUnit`
- `CardKBUnit`
- `JoystickUnit`, `Joystick2Unit`
- `EncoderUnit`, `Encoder8Unit`, `ExtEncoderUnit`
- `AngleUnit`, `Angle8Unit`
- `FaderUnit`
- `KeyUnit`
- `RotaryUnit`
- `ScrollUnit`

**Environmental Sensors:**
- `ENVUnit`, `ENVPROUnit`
- `CO2Unit`, `CO2LUnit`
- `TVOCUnit`
- `LightUnit`, `DLightUnit`
- `EarthUnit`
- `TubePressureUnit`

**Motion/Position:**
- `AccelUnit`
- `IMUUnit`, `IMUProUnit`
- `GestureUnit` (PAJ7620)
- `PIRUnit`
- `ToFUnit`, `ToF90Unit`, `ToF4MUnit`
- `UltrasoundI2CUnit`, `UltrasoundIOUnit`

**Temperature:**
- `NCIRUnit`, `NCIR2Unit`
- `ThermalUnit`, `Thermal2Unit`
- `KMeterUnit`, `KMeterISOUnit`
- `TMOSUnit`

**Output:**
- `RelayUnit`, `Relay2Unit`, `Relay4Unit`
- `BuzzerUnit`
- `VibratorUnit`
- `RGBUnit`
- `Servo180Unit`, `Servo360Unit`, `Servos8Unit`
- `FanUnit`
- `SSRUnit`, `ACSSRUnit`
- `FlashLightUnit`
- `LaserTXUnit`, `LaserRXUnit`

**Display:**
- `LCDUnit`
- `OLEDUnit`, `MiniOLEDUnit`
- `GlassUnit`, `Glass2Unit`
- `DigiClockUnit`

**Communication:**
- `RFIDUnit`, `UHFRFIDUnit`
- `IRUnit`
- `RS485Unit`, `ISO485Unit`
- `CANUnit`
- `ZigbeeUnit`
- `UWBUnit`
- `RF433RUnit`, `RF433TUnit`

**LoRa/Cellular:**
- `LoRaE220433Unit`, `LoRaE220JPUnit`
- `LoRaWANUnit`, `LoRaWANUnit_RUI3`
- `Cat1Unit`
- `CATMUnit`, `CATMGNSSUnit`
- `NBIOTUnit`, `NBIOT2Unit`

**ADC/DAC/Power:**
- `ADCUnit`, `ADCV11Unit`
- `DACUnit`, `DAC2Unit`
- `VoltmeterUnit`
- `AMeterUnit`
- `INA226Unit`
- `ACMeasureUnit`
- `OPUnit`
- `TimerPWRUnit`

**Audio:**
- `SynthUnit` (SAM2695)
- `MIDIUnit`
- `AudioPlayerUnit`
- `PDMUnit`

**GPS/Location:**
- `GPSUnit`, `GPSV11Unit`

**Weight/Scale:**
- `WeightUnit`, `WeightI2CUnit`
- `ScalesUnit`, `MiniScaleUnit`

**Motor/Motion Control:**
- `BLDCDriverUnit`
- `HbridgeUnit`
- `Step16Unit`
- `Roller485Unit`, `RollerCANUnit`

**I/O Expanders:**
- `EXTIOUnit`, `EXTIO2Unit`
- `PAHUBUnit`, `PBHUBUnit`
- `Grove2GroveUnit`

**Biometric:**
- `FingerUnit`, `Fingerprint2Unit`
- `HeartUnit`

**Misc:**
- `QRCodeUnit`
- `RCAUnit`
- `ReflectiveIRUnit`
- `RTC8563Unit`
- `ColorUnit`
- `HallEffectUnit`
- `LIMITUnit`
- `MQUnit`
- `IDUnit`
- `CatchUnit`
- `DDSUnit`
- `WateringUnit`
- `NECOUnit`
- `PuzzleUnit`
- `BPSUnit`
- `ASRUnit`
- `GatewayH2Unit`
- `MQTTUnit`, `MQTTPoEUnit`
- `DMX512Unit`

## Utilities

```python
import boot_option
import color_conv
import attitude_estimator
import label_plus
import pid
import warnings
import image_plus
from utility import exception_helper
```

## NOT Included

- `startup/*` - UIFlow2 cloud pairing
- `ezdata` - Cloud data sync
- `lv_utils` - LVGL (too large)

## Examples

```python
# Initialize M5
import M5
M5.begin()
print(f"Board: {M5.getBoard()}")  # 24 = CardputerADV

# Display
M5.Lcd.fillScreen(0x000000)
M5.Lcd.setTextColor(0xFFFFFF)
M5.Lcd.setCursor(10, 10)
M5.Lcd.println("Hello CardputerADV!")

# Speaker
M5.Speaker.tone(440, 200)  # A4 for 200ms

# WiFi
import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SSID', 'password')

# Keyboard
from hardware import MatrixKeyboard
kb = MatrixKeyboard()
key = kb.get_key()

# USB Keyboard
from usb.device.keyboard import Keyboard
kbd = Keyboard()
kbd.send_string("Hello!")

# Web Server
from microdot import Microdot
app = Microdot()
@app.route('/')
def index(req): return 'Hello!'
app.run(port=80)

# MQTT
from umqtt.simple import MQTTClient
c = MQTTClient("id", "broker.hivemq.com")
c.connect()
c.publish("topic", "msg")

# LoRa (using Cap module)
from cap import LoRa1262Cap
lora = LoRa1262Cap()
lora.send(b"Hello!")

# GPS Cap
from cap import GPSCap
gps = GPSCap()
lat, lon = gps.get_position()

# Unit example (correct class name)
from unit import CardKBUnit
kb = CardKBUnit()
key = kb.get_key()
```

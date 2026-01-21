# SPDX-FileCopyrightText: 2024 M5Stack Technology CO LTD
#
# SPDX-License-Identifier: MIT
#
# CardputerADV Custom - Cloud-free manifest
#
# This manifest explicitly includes only the modules needed for standalone
# MicroPython apps, excluding UIFlow2 cloud/startup components.
#
# Excluded:
#   - modules/startup/ (CloudApp, pairing UI, etc.)
#   - libs/ezdata/ (cloud data sync)
#   - libs/lv_utils/ (LVGL - deferred to future work)
#
# Included:
#   - Core MicroPython stdlib (asyncio, network, etc.)
#   - M5Stack hardware drivers (M5.Lcd, M5.Speaker, etc.)
#   - libs/hardware/ (MatrixKeyboard for I2C keyboard)
#   - widgets/ (M5.Widgets.FONTS)

# ============================================================================
# Core MicroPython modules from boards/manifest.py
# ============================================================================
require("mip")
require("ntptime")
require("dht")
require("onewire")
include("$(MPY_DIR)/extmod/asyncio")
require("webrepl")
require("upysh")
require("ssl")

# ============================================================================
# Core modules from m5stack/modules/manifest.py
# ============================================================================
module("_boot.py", base_path="$(MPY_DIR)/../m5stack/modules")
module("flashbdev.py", base_path="$(MPY_DIR)/../m5stack/modules")
module("inisetup.py", base_path="$(MPY_DIR)/../m5stack/modules")
include("$(MPY_DIR)/../m5stack/modules/widgets/manifest.py")
module("espnow.py", base_path="$(MPY_DIR)/../m5stack/modules")
require("lora-sync")
require("lora-sx126x")
require("lora-sx127x")

# ============================================================================
# Essential libs from libs/manifest_basic.py
# (Excluding ezdata, lv_utils which are cloud/LVGL related)
# ============================================================================
include("$(MPY_DIR)/../m5stack/libs/bleuart/manifest.py")
include("$(MPY_DIR)/../m5stack/libs/driver/manifest.py")
include("$(MPY_DIR)/../m5stack/libs/software/manifest.py")
# EXCLUDED: include("$(MPY_DIR)/../m5stack/libs/ezdata/manifest.py")
include("$(MPY_DIR)/../m5stack/libs/hardware/manifest.py")
include("$(MPY_DIR)/../m5stack/libs/image_plus/manifest.py")
# EXCLUDED: include("$(MPY_DIR)/../m5stack/libs/lv_utils/manifest.py")
include("$(MPY_DIR)/../m5stack/libs/m5ble/manifest.py")
include("$(MPY_DIR)/../m5stack/libs/m5espnow/manifest.py")
include("$(MPY_DIR)/../m5stack/libs/modbus/modbus/manifest.py")
include("$(MPY_DIR)/../m5stack/libs/requests2/manifest.py")
include("$(MPY_DIR)/../m5stack/libs/umqtt/manifest.py")
include("$(MPY_DIR)/../m5stack/libs/unit/manifest.py")
include("$(MPY_DIR)/../m5stack/libs/utility/manifest.py")
module("boot_option.py", base_path="$(MPY_DIR)/../m5stack/libs")
module("color_conv.py", base_path="$(MPY_DIR)/../m5stack/libs")
module("attitude_estimator.py", base_path="$(MPY_DIR)/../m5stack/libs")
module("label_plus.py", base_path="$(MPY_DIR)/../m5stack/libs")
module("pid.py", base_path="$(MPY_DIR)/../m5stack/libs")
include("$(MPY_DIR)/../m5stack/libs/iot_devices/manifest.py")
module("warnings.py", base_path="$(MPY_DIR)/../m5stack/libs")

# ============================================================================
# Additional board-specific libs from original CardputerADV manifest
# (Excluding startup modules)
# ============================================================================
# EXCLUDED: include("$(MPY_DIR)/../m5stack/modules/startup/manifest_cardputeradv.py")
include("$(MPY_DIR)/../m5stack/libs/cap/manifest.py")
include("$(MPY_DIR)/../m5stack/libs/chain/manifest.py")

# ============================================================================
# Additional useful libraries
# ============================================================================
include("$(MPY_DIR)/../m5stack/libs/microdot/manifest.py")
include("$(MPY_DIR)/../m5stack/libs/uftpd/manifest.py")
include("$(MPY_DIR)/../m5stack/libs/usb/manifest.py")
require("aiorepl")  # Async REPL over network
require("uaiohttpclient")  # Async HTTP client

#!/bin/bash
# Generate firmware_info.py from git tag
# Usage: ./gen-firmware-info.sh [--mini]

set -e

VERSION=$(git describe --tags 2>/dev/null || echo "v0.0.0")
VERSION="${VERSION#v}"  # strip leading v

if [ "$1" = "--mini" ]; then
    VERSION="${VERSION/therealhaoliu/therealhaoliu.mini}"
    VERSION="${VERSION/custom/custom.mini}"
fi

UPSTREAM="${VERSION%%+*}"

cat << EOF
# CardputerADV Custom Firmware version info
# Auto-generated from: git describe --tags

UPSTREAM_VERSION = "${UPSTREAM}"
CUSTOM_VERSION = "${VERSION}"
EOF

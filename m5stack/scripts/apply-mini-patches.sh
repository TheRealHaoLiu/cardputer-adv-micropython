#!/bin/bash
# Toggle mini variant patches (swaps CJK fonts for stubs in CMakeLists.txt)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CMAKE_FILE="$SCRIPT_DIR/../components/M5Unified/CMakeLists.txt"
CMAKE_BACKUP="$SCRIPT_DIR/../components/M5Unified/CMakeLists.txt.orig"

apply() {
    if grep -q "cjk_font_stubs.c" "$CMAKE_FILE"; then
        echo "Already in mini mode"
        exit 0
    fi

    cp "$CMAKE_FILE" "$CMAKE_BACKUP"
    sed -i.tmp -e 's|M5GFX/src/lgfx/Fonts/efont/\*.c|cjk_font_stubs.c|' \
               -e '/M5GFX\/src\/lgfx\/Fonts\/IPA\/\*.c/d' "$CMAKE_FILE"
    rm -f "$CMAKE_FILE.tmp"
    echo "Mini patches applied"
}

revert() {
    if [ -f "$CMAKE_BACKUP" ]; then
        mv "$CMAKE_BACKUP" "$CMAKE_FILE"
        echo "Mini patches reverted"
    else
        echo "Nothing to revert"
    fi
}

status() {
    if grep -q "cjk_font_stubs.c" "$CMAKE_FILE"; then
        echo "mini"
    else
        echo "normal"
    fi
}

case "${1:-status}" in
    apply)  apply ;;
    revert) revert ;;
    status) status ;;
    *)      echo "Usage: $0 {apply|revert|status}" ;;
esac

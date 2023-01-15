#!/usr/bin/env bash
set -euo pipefail

displayName=$1

node_modules/.bin/yo code \
    --extensionType ts \
    --extensionDisplayName "${displayName}" \
    --pkgManager npm \
    -q -o

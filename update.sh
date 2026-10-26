#!/usr/bin/env bash
# GEO Optimizer — Update Script
# Usage: bash update.sh

set -e

GREEN='\033[0;32m'
NC='\033[0m'
ok() { echo -e "${GREEN}\u2705 $1${NC}"; }

echo ""
echo "\U0001f504 GEO Optimizer — Updating..."
echo ""

CURRENT=$(geo --version 2>/dev/null || echo "not installed")
echo "   Current: $CURRENT"

pip install --upgrade geo-optimizer-skill
ok "Updated to latest version"

NEW=$(geo --version 2>/dev/null)
echo "   Latest:  $NEW"

echo ""
ok "GEO Optimizer updated successfully!"
echo ""
echo "\U0001f4d6 Changelog: https://github.com/auriti-labs/geo-optimizer-skill/blob/main/CHANGELOG.md"
echo ""

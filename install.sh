#!/usr/bin/env bash
# GEO Optimizer — Installation Script
# https://github.com/auriti-labs/geo-optimizer-skill
#
# Usage:
#   curl -sSL https://raw.githubusercontent.com/auriti-labs/geo-optimizer-skill/main/install.sh | bash
#   pip install geo-optimizer-skill

set -e

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

ok()  { echo -e "${GREEN}\u2705 $1${NC}"; }
err() { echo -e "${RED}\u274c $1${NC}"; exit 1; }

echo ""
echo "\U0001f916 GEO Optimizer — Installation"
echo "================================"
echo ""

# Verifica Python
command -v python3 >/dev/null 2>&1 || err "Python 3 is required. Install it first: https://python.org"
PYTHON_VER=$(python3 --version 2>&1)
ok "Python found: $PYTHON_VER"

# Installa da PyPI
echo ""
echo "\U0001f4e6 Installing geo-optimizer-skill from PyPI..."
pip install geo-optimizer-skill
ok "geo-optimizer-skill installed"

# Verifica
echo ""
geo --version && ok "CLI ready!" || err "Installation failed"

echo ""
echo "================================"
ok "Installation complete!"
echo ""
echo "\U0001f680 Quick start:"
echo "   geo audit --url https://yoursite.com"
echo "   geo llms --base-url https://yoursite.com --output llms.txt"
echo "   geo schema --type faq --url https://yoursite.com"
echo ""
echo "\U0001f4d6 Full docs: https://github.com/auriti-labs/geo-optimizer-skill"
echo ""

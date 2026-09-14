#!/bin/bash
GREEN="\033[1;32m"
CYAN="\033[1;36m"
YELLOW="\033[1;33m"
RED="\033[1;31m"
RESET="\033[0m"

clear
echo -e "${CYAN}╔═══════════════════════════════════════╗${RESET}"
echo -e "${CYAN}║     ${GREEN}NICS AUTOMATED INSTALLER${CYAN}          ║${RESET}"
echo -e "${CYAN}╚═══════════════════════════════════════╝${RESET}\n"

echo -e "${YELLOW}[*] Updating system packages...${RESET}"
pkg update -y && pkg upgrade -y

echo -e "${YELLOW}\n[*] Installing Python and Git...${RESET}"
pkg install python git -y

echo -e "${YELLOW}\n[*] Cloning the GitHub Repository...${RESET}"

git clone https://github.com/NICS404/NICS-FB-CLONING-2026.git

cd NICS-FB-CLONING-2026 || { echo -e "${RED}[!] Error: Directory not found!${RESET}"; exit 1; }

echo -e "${YELLOW}\n[*] Installing Python modules...${RESET}"
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    pip install requests
fi

echo -e "${GREEN}\n[+] Installation Complete! Starting NICS System...${RESET}"
sleep 2
python NICS.py

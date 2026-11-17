#!/bin/bash

echo "=========================================="
echo "      SETTING UP & STARTING HACKME        "
echo "=========================================="

# Check if Python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "[!] Python3 is not installed. Please install Python3 first."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "[*] Creating virtual environment (venv)..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "[*] Activating virtual environment..."
source venv/bin/activate

# Upgrade pip and install requirements silently
echo "[*] Installing required dependencies..."
pip install --upgrade pip > /dev/null 2>&1
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "[!] requirements.txt not found! Installing default packages..."
    pip install requests rich phonenumbers
fi

echo "[+] Setup complete! Starting Hackme Suite..."
echo "=========================================="

# Run the main scanner script
python3 scanner.py

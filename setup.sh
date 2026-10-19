#!/bin/bash

echo "=========================================="
echo " Setting up environment for CEO Projects "
echo "=========================================="

# Update package lists
sudo apt update -y

# Install essential system tools needed for security & python tools
sudo apt install -y python3 python3-pip python3-venv git nmap net-tools curl wget

# Create a virtual environment to prevent package conflicts on Kali
python3 -m venv venv
source venv/bin/activate

# Upgrade pip inside virtual environment
pip install --upgrade pip

# Install common Python security & scraping dependencies
pip install \
    requests \
    beautifulsoup4 \
    scapy \
    python-nmap \
    pandas \
    colorama \
    paramiko \
    fake-useragent

echo "=========================================="
echo " Setup Complete!                          "
echo " To start using your tools, run:          "
echo " source venv/bin/activate                 "
echo "=========================================="

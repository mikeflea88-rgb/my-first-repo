#!/bin/bash

echo "=========================================="
echo " Setting up environment for CEO Projects "
echo "=========================================="

# Update system packages
sudo apt update && sudo apt upgrade -y

# Install essential system dependencies and Python tools
sudo apt install -y python3 python3-pip python3-venv git nmap curl

# Create a virtual environment (recommended for Kali)
python3 -m venv venv
source venv/bin/activate

# Install Python packages often used in network & recon tools
pip install --upgrade pip
pip install requests beautifulsoup4 pandas scapy colorama

echo "=========================================="
echo " Setup Complete! Activate venv using:     "
echo " source venv/bin/activate                "
echo "=========================================="

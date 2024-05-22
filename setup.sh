#!/bin/bash
# Update package lists
sudo apt-get update

# Install TA-Lib dependencies
sudo apt-get install -y build-essential libta-lib0 libta-lib0-dev

# Install Python dependencies
pip install -r requirements.txt
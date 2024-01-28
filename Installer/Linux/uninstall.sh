#!/bin/bash

# Remove the executable
sudo rm /usr/local/bin/password_generator

# Remove the desktop launcher
sudo rm /usr/share/applications/password_generator.desktop

# Remove the icon (optional)    
sudo rm /usr/local/bin/seal.png

# Cleanup
rm -rf build dist __pycache__ PyPassGen.spec

echo "Password Generator has been uninstalled."

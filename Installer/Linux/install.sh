# Build the executable
pyinstaller --onefile PyPassGen.py

# Move the executable and icon to /usr/local/bin
sudo mv dist/password_generator /usr/local/bin
sudo cp src/seal.png /usr/local/bin

# Move the desktop launcher to the applications directory
sudo cp password_generator.desktop /usr/share/applications/

# Cleanup
rm -rf build dist __pycache__ PyPassGen.spec

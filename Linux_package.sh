chmod +x Installer/Linux/uninstall.sh
chmod +x Installer/Linux/install.sh
mkdir Installer/Linux/PyPassGen_Linux
mkdir Installer/Linux/PyPassGen_Linux/src
cp PyPassGen.py PyPassGen_Linux/
cp Installer/Linux/install.sh Installer/Linux/PyPassGen_Linux/
cp Installer/Linux/uninstall.sh Installer/Linux/PyPassGen_Linux/
cp Installer/Linux/password_generator.desktop Installer/Linux/PyPassGen_Linux/
cp src/seal.png PyPassGen_Linux/src/
tar -czvf PyPassGen_Linux.tar.gz PyPassGen_Linux

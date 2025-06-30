#!/bin/bash

sudo apt update && sudo apt install -y git gcc pkg-config make libsdl2-dev libserialport-dev
git clone https://github.com/laamaa/m8c.git
cd m8c
sed -i '/atexit(SDL_Quit);/a \ \ SDL_ShowCursor(SDL_DISABLE);' src/render.c
make
sudo make install
cd ..

sudo apt install -y jackd2 jack-tools jack-example-tools a2jmidid libzita-alsa-pcmi0 evtest python3-evdev brightnessctl

sudo usermod -aG audio $USER
sudo usermod -aG input $USER
sudo usermod -aG video $USER

sudo sysctl -w kernel.sched_rt_runtime_us=-1

cp config.ini /home/$USER/.local/share/m8c/config.ini
cp jackm8c.sh /home/$USER/jackm8c.sh
chmod +x /home/$USER/jackm8c.sh
sudo cp audio.conf /etc/security/limits.d/audio.conf
sudo cp gpio-keys-vol.py /usr/local/bin/gpio-keys-vol.py
sudo chmod +x /usr/local/bin/gpio-keys-vol.py
sudo cp gpio-keys-vol.service /etc/systemd/system/gpio-keys-vol.service 
sudo cp audiomidi.service /etc/systemd/system/audiomidi.service
sudo cp m8c.service /etc/systemd/system/m8c.service

sudo systemctl enable m8c.service
sudo systemctl enable audiomidi.service
sudo systemctl enable gpio-keys-vol.service


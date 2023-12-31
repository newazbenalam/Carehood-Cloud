#!/bin/bash
git clone https://github.com/newazbenalam/Carehood-Cloud
cd Carehood-Cloud || exit
sudo apt-get update -y
sudo apt install python3-pip -y
sudo apt install apache2 apache2-utils ssl-cert libapache2-mod-wsgi-py3 -y
pip install -r requirements.txt -y
sudo setcap 'cap_net_bind_service=+ep' /usr/bin/python3.10
sudo setcap 'cap_net_bind_service=+ep' /usr/bin/python3
sudo systemctl stop apache2
sudo systemctl disable apache2
python3 app.py
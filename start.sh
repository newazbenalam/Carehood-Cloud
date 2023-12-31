# #!/bin/bash
# git clone https://github.com/newazbenalam/Carehood-Cloud
# cd Carehood-Cloud || exit
# sudo apt-get update -y
# sudo apt install python3-pip -y
# sudo apt install apache2 apache2-utils ssl-cert libapache2-mod-wsgi-py3 -y
# pip install -r requirements.txt -y
# sudo setcap 'cap_net_bind_service=+ep' /usr/bin/python3.10
# sudo setcap 'cap_net_bind_service=+ep' /usr/bin/python3
# sudo systemctl stop apache2
# sudo systemctl disable apache2
# python3 app.py


#!/bin/bash
sudo apt-get update -y
sudo apt install -y python3-pip apache2 apache2-utils ssl-cert libapache2-mod-wsgi-py3
# Clone the repository
git clone https://github.com/newazbenalam/Carehood-Cloud /home/ubuntu/Carehood-Cloud
pip3 install -r /home/ubuntu/Carehood-Cloud/requirements.txt

echo "# Flask secret key
SECRET_KEY='gjr39dkjn344_!67#'
# Database URI for SQLAlchemy
SQLALCHEMY_DATABASE_URI='mysql://mysql:12345@192.168.0.72:3306/carehood'
# HOST and PORT for Flask
HOST=0.0.0.0
PORT=80
DEBUG=false" > /home/ubuntu/Carehood-Cloud/.env

# Grant capabilities to bind to privileged ports
sudo setcap 'cap_net_bind_service=+ep' /usr/bin/python3.10
sudo setcap 'cap_net_bind_service=+ep' /usr/bin/python3

# Stop and disable Apache (if running)
sudo systemctl stop apache2
sudo systemctl disable apache2

# Run your Flask application
sudo cp /home/ubuntu/Carehood-Cloud/myflaskapp.service /etc/systemd/system/myflaskapp.service

sudo systemctl daemon-reload
sudo systemctl enable myflaskapp
sudo systemctl start myflaskapp



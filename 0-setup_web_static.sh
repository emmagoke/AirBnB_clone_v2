#!/usr/bin/env bash
# This bash script sets up your web servers for the deployment of web_static.

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

html_="<h1>Welcome to My World</h1>"
echo "$html_" >> /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -hR ubuntu:ubuntu /data/

hbnb_url="\tlocation /hbnb_static/ {\t\t\nalias /data/web_static/current/;\t\t\nautoindex off;\t}"
sudo sed -i "29i\ $hbnb_url" /etc/nginx/sites-avaliable/default

service nginx restart

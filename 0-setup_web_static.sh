#!/usr/bin/env bash
# This bash script sets up your web servers for the deployment of web_static.

sudo apt -y install nginx

mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

html_="
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"
echo "$html_" >> /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown ubuntu:ubuntu 

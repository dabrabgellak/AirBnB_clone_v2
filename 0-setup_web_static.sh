#!/usr/bin/env bash 
#Sets up the web servers for the deployment of web_static

#Installs nginx 
sudo apt-get update
sudo apt-get -y install nginx
#Creation of folders
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
#Fake html file content
{
    echo "<html>"
    echo "<head> </head>"
    echo "<body>"
    echo "Holberton School"
    echo "</body>"
    echo "</html>"
} > /data/web_static/releases/test/index.html
#Symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current
#Changing permissions
sudo chown -R ubuntu:ubuntu /data/
#Update nginx configuration
sed -ie "60i location /hbnb_static {\nalias \/data\/web_static\/current\/;\nautoindex off;\n}" /etc/nginx/sites-available/default
service nginx restart

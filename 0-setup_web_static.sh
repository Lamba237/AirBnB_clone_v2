#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx

mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

echo "<html><head></head><body>Nginx config test page</body></html>"

rm -rf /data/web_static/current
sudo ln -rs /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

conf_file="/etc/nginx/sites-available/default"
sudo sed -i '/^\s*location \/static\/ {/a \\talias /data/web_static/current/;' "$conf_file"

sudo service restart nginx

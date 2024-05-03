#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

USER="ubuntu"
GROUP="ubuntu"

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
  echo "Installing Nginx..."
  sudo apt update && sudo apt install -y nginx
fi

# Create data directory with ownership
sudo mkdir -p /data && sudo chown -R ${USER}:${GROUP} /data

# Create subdirectories within data
for dir in web_static releases/test releases shared; do
  sudo mkdir -p "/data/$dir" && sudo chown -R ${USER}:${GROUP} "/data/$dir"
done

# Create a fake HTML file
echo "<h1>hbnb Static Content</h1>" | sudo tee /data/web_static/releases/test/index.html

# Update symbolic link
sudo rm -f /data/web_static/current && sudo ln -s /data/web_static/releases/test /data/web_static/current

# Update Nginx configuration
sudo cat <<EOF > /etc/nginx/sites-available/hbnb_static.conf
server {
  listen 80;
  server_name localhost;

  location /hbnb_static/ {
    alias /data/web_static/current/;
    index index.html index.htm;
  }
}
EOF

# Enable the new configuration and restart Nginx
sudo ln -s /etc/nginx/sites-available/hbnb_static.conf /etc/nginx/sites-enabled/
sudo systemctl restart nginx

echo "Web server setup complete!"

#!/usr/bin/env bash
# uses puppet to install nginx

exec { 'command':
  command  => ' sudo apt-get -y update;
  sudo apt-get install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;"\
  /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
}
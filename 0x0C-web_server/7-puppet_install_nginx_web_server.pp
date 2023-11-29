#!/usr/bin/env bash
# install server

package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => running,
  enable => true,
}

# Configure Nginx site
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;

      root /var/www/html;
      index index.html index.htm index.nginx-debian.html;

      server_name _;

      location / {
        return 200 'Hello World!';
      }

      location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
      }
    }
  ",
  notify  => Service['nginx'],
}

# Create the Hello World page
file { '/var/www/html/index.nginx-debian.html':
  ensure  => file,
  content => 'Hello World!',
}
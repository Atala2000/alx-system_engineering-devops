#changing the ULIMIT of nginx server

exec { 'changing ULIMIT':
command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',

path    => '/usr/local/bin/:/bin/',
}

exec { 'restarting server':
command => '/etc/init.d/nginx restart',

path    => '/etc/init.d/',
}

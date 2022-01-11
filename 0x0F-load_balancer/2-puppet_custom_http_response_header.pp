# Pupper manifet to install nginx and others requirements

$str = "add_header X-Served-By ${hostname};"

exec { 'update':
  command => '/usr/bin/apt-get update',
}
-> package { 'nginx':
  ensure  => installed,
  require => Exec['update']
}
-> file_line { 'Add redirection, 301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://twitter.com/Luffy_981 permanent;',
}
-> file_line { 'Add custom HTTP server':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => $str,
}
-> file { '/var/www/html/index.html':
  content => 'Hello World',
}
-> service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

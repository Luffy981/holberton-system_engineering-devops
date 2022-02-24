# Debug done !

exec { 'Change the limit':
  command => 'sed -i s/15/4096/ /etc/default/nginx',
  path    => '/bin'
}

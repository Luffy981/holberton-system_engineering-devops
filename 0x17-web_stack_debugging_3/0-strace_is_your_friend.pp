# Wordpress server debugged

exec { 'Fix php reference extension':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/bin'
}

# Fixed the bug
exec {'Updating limits to Holberton User':
  command  => "sed -i 's/holberton soft nofile.*/holberton soft nofile 9000/' /etc/security/limits.conf",
  provider => shell
}
exec {'Updating limit to Holberton User':
  command  => "sed -i 's/holberton hard nofile.*/holberton hard nofile 9000/' /etc/security/limits.conf",
  provider => shell
}

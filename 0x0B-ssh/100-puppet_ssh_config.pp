# Your SSH client configuration must be configured to use the private key ~/.ssh/school
# Your SSH client configuration must be configured to refuse to authenticate using a password

file_line {
  path => '/etc/ssh/ssh_config',
  ensure => 'present'
  line => '	IdentityFile ~/.ssh/school'
}

file_line {
  path => '/etc/ssh/ssh_config',
  ensure => 'present'
  line => '	PasswordAuthentication no'
}

# Execute a command
exec { 'I_KILLED_YOU_BITCH':
  command  => 'pkill -f killmenow',
  provider => shell,
}


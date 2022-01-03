# Execute a command
exec { 'I_KILL_YOU_BITCH':
	command => 'pkill -f killmenow',
	provider => shell,
}


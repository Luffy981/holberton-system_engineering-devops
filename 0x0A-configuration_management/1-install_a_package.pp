# Install a package
package { 'puppet-lint':
    ensure             => '2.5.0',
    provider           => 'gem',
  reinstall_on_refresh => true,
}

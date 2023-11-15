# Fixing error 500 in apache server with puppet

exec { 'webstack_debug':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
exec { 'nginx-restart':
  require => Exec['webstack_debug'],
  command => 'nginx restart',
  path    => '/etc/init.d/'
}

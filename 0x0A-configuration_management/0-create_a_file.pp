file { '/tmp/school':
  mode => '0744',
  ensure => present,
  owner => 'www-data',
  group => 'www-data',
  content => 'I love Puppet',
}

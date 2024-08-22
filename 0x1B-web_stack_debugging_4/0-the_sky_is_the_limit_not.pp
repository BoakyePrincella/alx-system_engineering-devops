# This is a puppet manifest to fix nginx

exec {'fix--for-nginx':
  command => "sed -i 's/.*ULIMIT.*/ULIMIT=\"-n 4096\"/g' /etc/default/nginx",
  path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin']
}

exec {'fix-for-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}

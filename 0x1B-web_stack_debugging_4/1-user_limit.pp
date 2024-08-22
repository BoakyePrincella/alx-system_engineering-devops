# This is a puppet manifest to grant ability to open as much files as possible

exec { 'sed -i "s/holberton hard nofile 5/holberton hard nofile 5000/" /etc/security/limits.conf':
  path => '/usr/bin:/usr/sbin:/bin',
}

exec { 'sed -i "s/holberton soft nofile 4/holberton soft nofile 4000/" /etc/security/limits.conf':
  path => '/usr/bin:/usr/sbin:/bin',
}

-> exec {'change-os-configuration-for-holberton-user':
  command => '/sbin/sysctl -p',
}

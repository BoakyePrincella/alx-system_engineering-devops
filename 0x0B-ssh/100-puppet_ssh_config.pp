#!/usr/bin/env bash
# This is a puppet manifest to configure ssh

file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '  PasswordAuthentication no',
}

file_line { 'Delare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '  IdentityFile ~/.ssh/school',
}

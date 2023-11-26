# puppet script
file_line { 'Turn off passwd auth':
  ensure => 'present,
  path => '/etc/ssh/ssh_config',
  line => '    PasswordAuthentication no'
}

file_line { 'Declare identity file':
  esnure => 'present',
  path => '/etc/ssh/ssh_config',
  line => '    identityFile ~/.ssh/school',
}
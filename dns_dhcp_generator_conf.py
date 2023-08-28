import re

PUPPET_DIRECTORY = '/etc/puppetlabs/code/environments/production/'
HOSTS_DIRECTORY = '/etc/puppetlabs/code/environments/production/dns-dhcp/'

FILE_BASE = '/etc/puppetlabs/files/'

VLANS = {
    '10.10.11':{
      'network': '10.10.11.0/24',
      'regex': re.compile('0?10[\.]0?10[\.]0?11[\.]'),
      'dns': True,
      'fwd_file' : 'monitor.inside.zone',
      'fwd_origins': ['monitor.'],
      'rev_file' : '10.10.11.inside.revzone',
      'rev_origins': [ '10.10' ],
      'dhcp_header': {
          'option subnet-mask': '255.255.255.0',
          'option domain-name': 'monitor',
          'option domain-name-servers': [ '10.10.11.5', '10.10.11.4' ],
          'option log-servers': [ '10.10.11.8' ],
          'option ntp-servers': [ '10.10.11.5', '10.10.11.4' ],
          'default-lease-time': 31557600,
          'min-lease-time': 31557600,
      },
    },
    '10.30'       : {  #zde bude pouze origin 10.30
      'network': '10.30.0.0/16',
      'regex'   : re.compile('0?10[\.]0?30[\.]'),
      'dns'     : True,
      'fwd_file': 'example2.example1.cz.inside.zone',
      'fwd_origins': ['example2.example1.cz.'],
      'rev_file': '10.30.inside.revzone',
      'rev_origins': [ '30.10' ],
      'dhcp_header': {
          'option subnet-mask': '255.255.0.0',
          'option routers': [ '10.30.0.39' ],
          'option domain-name': 'example2.example1.cz',
          'option domain-name-servers': [ '10.30.0.37', '10.30.0.38' ],
          'option log-servers': [ '147.231.25.201' ],
          'option ntp-servers': [ '10.30.0.37', '10.30.0.38' ],
          'allow': 'unknown-clients',
          'range': '10.30.0.64 10.30.0.253',
          'default-lease-time': 31557600,
          'min-lease-time': 31557600,
          'include': '"/etc/dhcp/dhcpd.mff-next-server.conf"',
      },
    },
    '10.6.51': {
      'network': '10.6.51.0/24',
      'regex'   : re.compile('0?10[\.]0?0?6[\.]0?51[\.]'),
      'dns'     : False,
      'dhcp_header': {
          'option subnet-mask': '255.255.255.0',
          'option domain-name': 'monitor',
          'option domain-name-servers': [ '10.6.51.2' ],
          'option log-servers': [ '10.6.51.2' ],
          'option ntp-servers': [ '10.6.51.2' ],
          'default-lease-time': 31557600,
          'min-lease-time': 31557600,
      },
    },
    '172.16'      : { # zde pouze origin 172.16
      'network': '172.16.0.0/16',
      'regex'   : re.compile('172[\.]0?16[\.]'),
      'dns'     : True,
      'fwd_file': 'example2.example1.cz.inside.zone',
      'fwd_origins': [ 'example2.example1.cz.' ],
      'rev_file': '172.16.inside.revzone',
      'rev_origins': [ '16.172', ],
      'dhcp_header': {
          'option domain-name': 'example2.example1.cz',
          'option domain-name-servers': [ '172.16.0.16', '172.16.0.15' ],
          'option interface-mtu': 1500,
          'option log-servers': [ '172.16.0.201' ],
          'option ntp-servers': [ '172.16.0.16', '172.16.0.15' ],
          'option domain-search': [ "example2.example1.cz", "example3.cz" ],
          'default-lease-time': 31557600,
          'min-lease-time': 31557600,
          'option routers': '172.16.0.39',
          'include': '"/etc/dhcp/dhcpd.wn-next-server.conf"',
      },
    },
    '192.168'     : {  # zde pouze origin 192.168
      'network': '192.168.0.0/16',
      'regex'    : re.compile('192[\.]168[\.]'),
      'dns'      : True,
      'fwd_file': 'monitor.inside.zone',
      'fwd_origins': [ 'monitor.' ],
      'rev_file': '192.168.inside.revzone',
      'rev_origins': [ '168.192', ],
      'dhcp_header': {
          'option domain-name': 'monitor',
          'option domain-name-servers': [ '192.168.1.5', '192.168.1.38' ],
          'option interface-mtu': 1500,
          'option log-servers': [ '192.168.1.34' ],
          'option ntp-servers': [ '192.168.1.5', '192.168.1.38' ],
          'option domain-search': [ "monitor" ],
          'default-lease-time': 31557600,
          'min-lease-time': 31557600,
      },
    },
    2001:db8:3333:4444:5555:6666:7777:8888
    '3333'     : {
      'network' : '2001:db8:3333:1::/64',
      'regex'   : re.compile('2001:db8:3333:0?0?0?1:'),
      'dns'     : False,
      'dhcp_header' : {
        'option dhcp6.name-servers': [ '2001:db8:3333:6025:1::20', '2001:db8:3333:6025:1::19' ],
        'option dhcp6.domain-search': [ 'example2.example1.cz', 'example3.cz' ],
        'option dhcp6.info-refresh-time': 21600,
        'option log-servers': [ 'syslog.example2.example1.cz' ],
        'option dhcp6.sntp-servers' : [ '2001:db8:3333:6025:1::20', '2001:db8:3333:6025:1::19' ],
        'default-lease-time': 31557600,
        'min-lease-time': 31557600,
        'preferred-lifetime': 23668200,
        'include': '"/etc/dhcp/dhcpd.farm-next-server.conf"',
      },
    },
   
    }
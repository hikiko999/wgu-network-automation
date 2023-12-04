inventory={
    'devices': {
        'IT_Network_switch': {
            'host': '10.10.1.5',
            'username': 'admin',
            'password': '',
            'device_type': 'extreme_exos',
            'configuration': {
                'vlan': {
                    'name': 'IT_VLAN',
                    'tag': '5',
                    'description': 'IT VLAN 5 FOR IT NETWORK'
                },
                'general': {
                    'name': 'IT_Network',
                    'ram': 512,
                    'vcpus': 1,
                    'qemu_binary': {
                        'path': '/usr/bin/qemu-system-x86_64',
                        'version': '4.2.1'
                    },
                    'boot_priority': 'CD/DVD-ROM_or_HDD',
                    'on_close': 'acpi',
                    'console_type': 'vnc'
                },
                'network': {
                    'adapters': 13,
                    'base_mac': '0c:1c:b2:85:00:00',
                    'type': 'rtl8139',
                    'replicate_states_qemu': True
                }
            }
        },
        'MGMT_Network_switch': {
            'host': '10.10.1.6',
            'username': 'admin',
            'password': '',
            'device_type': 'extreme_exos',
            'configuration': {
                'vlan': {
                    'name': 'MGMT_VLAN',
                    'tag': '10',
                    'description': 'MGMT VLAN 10 FOR MANAGEMENT NETWORK'
                },
                'general': {
                    'name': 'MGMT_Network',
                    'ram': 512,
                    'vcpus': 1,
                    'qemu_binary': {
                        'path': '/usr/bin/qemu-system-x86_64',
                        'version': '4.2.1'
                    },
                    'boot_priority': 'CD/DVD-ROM_or_HDD',
                    'on_close': 'acpi',
                    'console-type': 'vnc'
                },
                'network': {
                    'adapters': 13,
                    'base_mac': '0c:cc:78:5d:00:00',
                    'type': 'rtl8139',
                    'replicate_states_qemu': True
                }
            }
        },
        'ACCT_Network_switch': {
            'host': '10.10.1.7',
            'username': 'admin',
            'password': '',
            'device_type': 'extreme_exos',
            'configuration': {
                'vlan': {
                    'name': 'ACCT_VLAN',
                    'tag': '15',
                    'description': 'ACCT VLAN 15 FOR ACCOUNTING NETWORK'
                },
                'general': {
                    'name': 'ACCT_Network',
                    'ram': 512,
                    'vcpus': 1,
                    'qemu_binary': {
                        'path': '/usr/bin/qemu-system-x86_64',
                        'version': '4.2.1'
                    },
                    'boot_priority': 'CD/DVD-ROM_or_HDD',
                    'on_close': 'acpi',
                    'console_type': 'vnc'
                },
                'network': {
                    'adapters': 13,
                    'base_mac': '0c:40:34:07:00:00',
                    'type': 'rtl8139',
                    'replicate_states_qemu': True
                }
            }
        },
        'User_Network_switch': {
            'host': '10.10.1.8',
            'username': 'admin',
            'password': '',
            'device_type': 'extreme_exos',
            'configuration': {
                'vlan': {
                    'name': 'USER_VLAN',
                    'tag': '20',
                    'description': 'USER VLAN 20 FOR USER NETWORK'
                },
                'general': {
                    'name': 'User_Network',
                    'ram': 512,
                    'vcpus': 1,
                    'qemu_binary': {
                        'path': '/usr/bin/qemu-system-x86_64',
                        'version': '4.2.1'
                    },
                    'boot_priority': 'CD/DVD-ROM_or_HDD',
                    'on_close': 'acpi',
                    'console_type': 'vnc'
                },
                'network': {
                    'adapters': 13,
                    'base_mac': '0c:e0:f2:0b:00:00',
                    'type': 'rtl8139',
                    'replicate_states_qemu': True
                }
            }
        }
    }
}
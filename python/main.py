from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, AuthenticationException
from paramiko.ssh_exception import SSHException

import sys
import yaml

#python script "inventory_file" "command_file"

inventory_file = sys.argv[1]
with open(f"./inventory/{inventory_file}.yml","r") as f:
    inventory_contents = yaml.load(f, Loader=yaml.SafeLoader)

command_file = f"./commands/{sys.argv[2]}"
def connect(host,username,password,device_type):
    
        client = ConnectHandler(host=host, username=username, password=password, device_type=device_type)
        output = client.send_config_from_file(command_file,read_timeout=30)
        print(output)
        print(f"Ending connection to {host}\n")
    
def looper(inventory):
    
    for i in inventory["devices"]:
        try:
            print(f"Connecting to {i}|{inventory['devices'][i]['host']}")
            connect(inventory["devices"][i]["host"],
                    inventory["devices"][i]["username"],
                    inventory["devices"][i]["password"],
                    inventory["devices"][i]["device_type"]
            )
        except AuthenticationException:
            print (f"Authentication Failure: {inventory['devices'][i]['host']}")
            continue
        except NetmikoTimeoutException:
            print (f"Timeout Failure: {inventory['devices'][i]['host']}")
            continue
        except SSHException:
            print (f"SSH Failure: {inventory['devices'][i]['host']}")
            continue

if __name__ == '__main__':
    looper(inventory_contents)

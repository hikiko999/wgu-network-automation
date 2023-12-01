from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, AuthenticationException
from paramiko.ssh_exception import SSHException
from datetime import datetime, timedelta

import sys
import yaml

#python3 script "inventory_file" "command_file"

inventory_file = sys.argv[1]
with open(f"./inventory/{inventory_file}","r") as f:
    inventory_contents = yaml.load(f, Loader=yaml.SafeLoader)

# datetime for output formatting
now = datetime.utcnow()
dt_string = now.strftime("%m-%d-%Y %H-%M-%S")
command_file = f"./commands/{sys.argv[2]}"
def connect(host,username,password,device_type,seq):
    
        client = ConnectHandler(host=host, username=username, password=password, device_type=device_type)
        output = client.send_config_from_file(command_file,read_timeout=90)
        print(output)
        with open(f"./outputs/{dt_string} {seq} {sys.argv[1]}-{sys.argv[2]}", "w") as f:
            f.write(f"LOG TIME ACCORDING TO UTC\n============================\n{output}")
        print(f"Ending connection to {host}\n")
    
def looper(inventory):
    seq = 0
    for i in inventory["devices"]:
        seq+=1
        try:
            print(f"Connecting to {i}|{inventory['devices'][i]['host']}")
            connect(inventory["devices"][i]["host"],
                    inventory["devices"][i]["username"],
                    inventory["devices"][i]["password"],
                    inventory["devices"][i]["device_type"],
                    seq
            )
        except AuthenticationException:
            failure_str = f"Authentication Failure: {inventory['devices'][i]['host']}"
            print(failure_str)
            with open(f"./outputs/{dt_string} {seq} {sys.argv[1]}-{sys.argv[2]} FAILED AuthenticationException", "w") as f:
                f.write(f"LOG TIME ACCORDING TO UTC\n============================\n{failure_str}")
            continue
        except NetmikoTimeoutException:
            failure_str = f"Timeout Failure: {inventory['devices'][i]['host']}"
            print(failure_str)
            with open(f"./outputs/{dt_string} {seq}  {sys.argv[1]}-{sys.argv[2]} FAILED NetmikoTimeoutException", "w") as f:
                f.write(f"LOG TIME ACCORDING TO UTC\n============================\n{failure_str}")
            continue
        except SSHException:
            failure_str =f"SSH Failure: {inventory['devices'][i]['host']}"
            print(failure_str)
            with open(f"./outputs/{dt_string} {seq}  {sys.argv[1]}-{sys.argv[2]} FAILED SSHException", "w") as f:
                f.write(f"LOG TIME ACCORDING TO UTC\n============================\n{failure_str}")
            continue

if __name__ == '__main__':
    looper(inventory_contents)

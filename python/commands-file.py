from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, AuthenticationException
from paramiko.ssh_exception import SSHException
from datetime import datetime, timedelta

import sys
import yaml

#python3 script "inventory_file" "command_file" "no/log"

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
        #output = client.send_command_timing(sys.argv[2],read_timeout=90,last_read=9.0)
        print(output)
        if sys.argv[3] == "log":
            with open(f"./outputs/{dt_string}-{seq}-{sys.argv[1]}-{sys.argv[2]}.log", "w") as f:
                f.write(f"LOG TIME ACCORDING TO UTC\n============================\n{output}")
        print(f"Ending connection to {host}\n")
    
def looper(inventory):
    seq_num = 0
    for i in inventory["devices"]:
        seq_num += 1
        seq = f"{i}({seq_num})"
        try:
            print(f"Connecting to {i}|{inventory['devices'][i]['host']}")
            connect(inventory["devices"][i]["host"],
                    inventory["devices"][i]["username"],
                    inventory["devices"][i]["password"],
                    inventory["devices"][i]["device_type"],
                    seq
            )
        except AuthenticationException as e:
            failure_str = f"Authentication Failure: {inventory['devices'][i]['host']}\n\n{e}"
            print(failure_str)
            if sys.argv[3] == "log":
                with open(f"./outputs/{dt_string}-{seq}-{sys.argv[1]}-{sys.argv[2]}-FAILED-AuthenticationException.log", "w") as f:
                    f.write(f"LOG TIME ACCORDING TO UTC\n============================\n{failure_str}")
            continue
        except NetmikoTimeoutException as e:
            failure_str = f"Timeout Failure: {inventory['devices'][i]['host']}\n\n{e}"
            print(failure_str)
            if sys.argv[3] == "log":
                with open(f"./outputs/{dt_string}-{seq}-{sys.argv[1]}-{sys.argv[2]}-FAILED-NetmikoTimeoutException.log", "w") as f:
                    f.write(f"LOG TIME ACCORDING TO UTC\n============================\n{failure_str}")
            continue
        except SSHException as e:
            failure_str =f"SSH Failure: {inventory['devices'][i]['host']}\n\n{e}"
            print(failure_str)
            if sys.argv[3] == "log":
                with open(f"./outputs/{dt_string}-{seq}-{sys.argv[1]}-{sys.argv[2]}-FAILED-SSHException.log", "w") as f:
                    f.write(f"LOG TIME ACCORDING TO UTC\n============================\n{failure_str}")
            continue

if __name__ == '__main__':
    looper(inventory_contents)

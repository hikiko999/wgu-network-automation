import yaml
import pprint

with open('./exos.yml', 'r') as f:
    inventory_contents = yaml.load(f, Loader=yaml.SafeLoader)

print(inventory_contents)

with open('./exos.py', 'w') as f:
    f.write(f"inventory = {str(inventory_contents)}")
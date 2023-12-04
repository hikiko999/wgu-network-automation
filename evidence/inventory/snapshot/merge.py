import os

output = ""

directory = './assets'

for filename in os.listdir(directory):
    file_path = os.path.join(directory,filename)
    if os.path.isfile(file_path):
        with open(file_path,"r") as f:
            content_raw = f.read()
            
        content = f"{filename}\n{content_raw}\n========\n"
        output += content


inventory_file = "./inventory.txt"
with open(inventory_file,"w") as f:
    f.write(output)
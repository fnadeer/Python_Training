import re
import os
cmd = 'clear'
os.system(cmd)
with open("show_version.txt") as f:
    output = f.read()
print(output)
print("-" * 80)
k = re.split(r"^----.*$", output, flags = re.M)
print(k)
#print(k[0])
rep = re.sub(r"^----.*$",'######WHATEVER######', output, flags = re.M) #Replacement
print(rep)
#e.findall

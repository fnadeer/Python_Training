import re
import os
cmd = 'clear'
os.system(cmd)
with open("show_version.txt") as f:
    output = f.read()

show_ver = output.splitlines()
line = show_ver[1]
print(line)
p = re.search(r"^Cisco(.*) Software (\S+), Version (?P<Serial_num>\S+), .*$", line)
k = re.search(r"^Cisco(.*)", line).group(1)
k = re.search(r"^Cisco(.*),", line).group(1)
#To reduce the greedy behaviour
k = re.search(r"^Cisco(.*?), ", line).group(1)
print(re.search(r"^Cisco(.*?), ", line).group(0))
print(re.search(r"^Cisco(.*?)", line).group(1)) #Grab as small as you can and have the pattern work, here space is gonna get printed
print(k)
# Finding the processor board id from show version
print(re.search(r"^Processor board ID(.*)$", output)) #No output is received as it latches on to the beginning of the file due to ^
serial_number = re.search(r"^Processor board ID(.*)$", output, flags = re.M).group(1)
print(serial_number)
print("-" * 80)
"""l=re.search(r"^Cisco.*", output, flags=re.DOTALL).group(0)#Kirk has output but for me 'None' is coming, python update?!
print(l)#Does work"""
serial_number = re.search(r"^Processor board ID(.*)$", output, flags = re.I).group(1) #Ignore capitalization in this flag

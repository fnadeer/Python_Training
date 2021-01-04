import re
import os
cmd = 'clear'
os.system(cmd)
with open("show_version.txt") as f:
    output = f.read()
show_ver = output.splitlines()
line = show_ver[1]
print(line)
print("-" * 80)


print(re.search(r"^Cisco(.*), Version (\S+), .*$", line).group(0))
print(re.search(r"^Cisco(.*), Version (\S+), .*$", line).group(1))
print(re.search(r"^Cisco(.*), Version (\S+), .*$", line).group(2))
os = re.search(r"^Cisco(.*) Software (\S+), Version (\S+), .*$", line).group(2)
k = re.search(r"^Cisco(.*) Software (\S+), Version (?P<Serial_num>\S+), .*$", line)
print(os)
print(k.groupdict())

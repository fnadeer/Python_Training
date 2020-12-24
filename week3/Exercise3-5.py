import os
command = 'clear'
os.system(command)
WINDOWS = False
base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
if WINDOWS:
    base_cmd = base_cmd_windows
else:
    base_cmd = base_cmd_linux
from pprint import pprint
ip_list = []
for i in range(0,254):
    i = '10.10.100.' + str(i+1)
    ip_list.append(i)
for index,ip in enumerate(ip_list):
    print("{} ---> {}".format(index,ip))
list_slice = ip_list[2:6]
print('-' * 80)
for ip_addr in list_slice:
    print("IP Addr: ", ip_addr)
    os.system("{} {}".format(base_cmd,ip_addr))
    print('-' * 80)
print()

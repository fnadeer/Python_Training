#Key value mapping
import os
cmd = 'clear'
os.system(cmd)
net_device = {}
print (type(net_device))
net_device['ip_addr'] = '192.168.1.1'
net_device = {'ip_addr2':'192.168.1.2','ip_addr': '192.168.1.1'}
var1 = 'Vendor'
net_device[var1] = 'Cisco'
net_device['Device Type'] = 'ios'
net_device['Gateway'] = '192.168.1.3'
print(net_device)
print(net_device['Vendor'])
net_device[var1] = 'Juniper'
print(net_device['Vendor'])
# NOTE: Dictionaries are mutable

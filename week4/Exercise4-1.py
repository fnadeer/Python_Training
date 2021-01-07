import pprint 
net_dev = {'ip_addr': '192.168.1.1','vendor': 'Cisco','Username' : 'admin', 'Password': 'password'}
print(net_dev['ip_addr'])
if 'Cisco'in net_dev.values():
    net_dev['Platform'] = 'ios'
if 'Juniper' in net_dev.values():
    net_dev['Platform'] = 'junos'
#print(net_dev)
bgp_fields = {'bgp_as':'18725', 'peer_as': '20475', 'peer_ip': '20.2.20.2'}
net_dev.update(bgp_fields)
for k in net_dev.keys():
    print(k)
for items in net_dev.items():
    print(items)

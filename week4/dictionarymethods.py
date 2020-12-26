net_device = {'ip_addr2': '192.168.1.2', 'ip_addr': '192.168.1.1', 'Vendor': 'Cisco', 'Device Type': 'ios', 'Gateway': '192.168.1.3'}
#Error handling
print(net_device.get('model'))
print(net_device.get('model', 'Error 500:Lookup failed'))
print(net_device.get('Vendor'))
#print(dir(net_device))
#net_device2 = net_device.copy()
#print(net_device2)
#print(net_device2 is net_device) #If false not pointing towards same memory
net_device['Model'] = 'ISR'
print(net_device)
print(net_device.pop('Model'))
print('-' * 80)
print(net_device)
net_device2 = {'Vendor':'Juniper', 'Model':'SRX'}
print(net_device2)
net_device.update(net_device2)
print('-' * 80)
print(net_device)
#For Loop
print('-' * 80)
#for key in net_device:
    #print(key)
#for values in net_device.values():
    #print(values)
for k,v in net_device.items():
    print(k,v)
    print('-' * 30)

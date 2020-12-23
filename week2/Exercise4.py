from pprint import pprint
with open("show_ip_int_brief.txt") as f:
    output = f.readlines()
output.pop(0)
f4_ip = output[4].strip()
print(f4_ip)
fields = (f4_ip.split())
intf = fields[0]
ipadd = fields[1]
my_tuple = (intf, ipadd)
pprint(my_tuple)
k = "192.168.1.1"
print(k.split("."))

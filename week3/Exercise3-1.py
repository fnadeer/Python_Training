"""from pprint import pprint
f = open("show_vlan.txt")
list1 = []
vlan_list = []
num_lines = len(f.readlines())
f.seek(0)
i=0
while i <num_lines:
    n = f.readline()
    if "-----" in n or "VLAN" in n or n.startswith("   "):
        continue
    else:
        list1.append(n)
    i = i + 1
for h in list1:
    member = h.split()
    vlan_list.append((member[0],member[1]))
print(vlan_list)"""

from pprint import pprint
with open("show_vlan.txt") as f:
    show_vlan = f.read()
vlan_list = []
show_vlan = show_vlan.splitlines()
for line in show_vlan:
    if "VLAN" in line or "-----" in line or line.startswith("   "):
        continue
    fields = line.split()
    vlan_id = fields[0]
    vlan_name = fields[1]
    vlan_list.append((vlan_id,vlan_name))
pprint(vlan_list)

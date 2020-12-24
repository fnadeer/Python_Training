#My Solution
"""with open("show_lldp_neighbors_detail.txt") as f:
    show_lldp = f.read()
show_lldp = show_lldp.splitlines()
found1,found2 = (False,False)
for line in show_lldp:
    fields = line.split()
    if fields[0]=='System' and fields[1]=='Name:':
        remot_name = fields[2]
        found1 = True
    if fields[0]=='Port' and fields[1]=='id:':
        remot_port = fields[2]
        found2 = True
    if found1 and found2:
        print("The System Name/ Pord ID: {} / {}".format(remot_name,remot_port))
        break"""
#Official Solution
with open("show_lldp_neighbors_detail.txt") as f:
    show_lldp = f.read()
show_lldp = show_lldp.splitlines()
found1,found2 = (False,False)
for line in show_lldp:
    if 'System Name:' in line:
        _,remot_name = line.split('System Name:')
        print(remot_name)
    elif 'Port id:' in line:
        _,remot_port = line.split('Port id:')
        print(remot_port)

from pprint import pprint
with open("show_arp.txt") as f:
    output = f.read()
output = output.splitlines()
i=0
found1,found2 = (False,False) #Just putting another flagging method
for line in output:
    if line.startswith("Protocol"):
        continue
    else:
        fields = line.split()
        ip_addr = fields[1]
        mac_addr = fields[3]

        if ip_addr == '10.220.88.1':
            pprint("Default gateway IP/MAC: {}/{}".format(ip_addr,mac_addr))
            i = i+1
            found1 = True
        if ip_addr == '10.220.88.30':
            pprint("Arista3 IP/MAC: {}/{}".format(ip_addr,mac_addr))
            i= i+1
            found2 = True
        if i==2 and found1 and found2:
            print("Exiting..")
            break

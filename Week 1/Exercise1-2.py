ipaddr = input("Please enter an IP address: ")
print("{:^20}{:^20}{:^20}{:^20}".format("Octet1","Octet2","Octet3","Octet4"))
print("-" * 80)
splitted = (ipaddr.split("."))
print("{:^20}{:^20}{:^20}{:^20}".format(splitted[0],splitted[1],splitted[2],splitted[3]))
print("{:^20}{:^20}{:^20}{:^20}".format(bin(int(splitted[0])),bin(int(splitted[1])),bin(int(splitted[2])),bin(int(splitted[3]))))
print("{:^20}{:^20}{:^20}{:^20}".format(hex(int(splitted[0])),hex(int(splitted[1])),hex(int(splitted[2])),hex(int(splitted[3]))))
print("-" * 80)

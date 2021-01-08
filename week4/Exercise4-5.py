import re
with open("show_ipv6_intf.txt") as f:
    output = f.read()
match = re.search(r"IPv6 address:\s+(.*)\s+IPv6 subnet:", output,flags = re.DOTALL)
ipv6_add = match.group(1).strip()
ipv6_list = ipv6_add.splitlines()
#print(ipv6_list)
for i, address in enumerate(ipv6_list):
    address = re.sub(r"\[VALID\]","",address)
    ipv6_list[i] = address.strip()

print(ipv6_list)

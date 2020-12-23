with open("show_arp.txt") as f:
    output = f.readlines()
out_mod = output[1:]
from pprint import pprint
print("-" * 80)
out_mod.sort()
pprint(out_mod)
print()
print("-" * 80)
nw_slice = out_mod[:3]
pprint(nw_slice)
print("-" * 80)
print("\n".join(nw_slice))

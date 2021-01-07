import re
show_version = '''
Cisco 881 (MPC3300) processor (revision 1.0) with 236/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)'''

match = re.search(r"^Cisco (?P<Model>\d+\s\S\w+\)).*with (?P<Memory_String>\w+/\w+).*$",show_version, flags = re.M)
print(match.groupdict())

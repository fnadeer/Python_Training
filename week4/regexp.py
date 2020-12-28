import re
line = "10.220.100.1"
ip_addr = line
print(re.search(r".", ip_addr))
print(re.search(r"X", ip_addr))
print(re.search(r"..", ip_addr).group(0))
print(re.search(r"...", ip_addr).group(0))
print(re.search(r"....", ip_addr).group(0))
#print(re.search(r"..","").group(0)) #Null string no match
print(re.search(r"....", "XXXX").group(0))
print(re.search(r".+",ip_addr).group(0)) #One or more times if .
print(re.search(r".*",ip_addr).group(0)) #Zero or more times, so match if the character is not there
print("-" * 80)
print(re.search(r"^.+$",ip_addr).group(0))
print(re.search(r".$",ip_addr).group(0)) #Prints from the end
print("-" * 80)
print(re.search(r"\d\d",ip_addr).group(0))
print("-" * 80)
#print(re.search(r"^\d\d\d",ip_addr))
print(re.search(r"^\d+",ip_addr).group(0))
print(re.search(r"\d+$",ip_addr).group(0))
ip_add = '       10.220.100.1     '
print(re.search(r"^\s+",ip_add))#.group(0))
print(re.search(r"^\s+\d+",ip_add))#.group(0))
print(re.search(r"^\s+\S+",ip_add))
print(re.search(r"^\s+[\d\.]+",ip_add))
print(re.search(r"^\s+(\S+)",ip_add)) #Belongs to group 0 , that is the whole output
print(re.search(r"^\s+(\S+)",ip_add).groups(1)) # For saving , each parenthesis belong each group

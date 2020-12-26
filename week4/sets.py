import os
cmd = 'clear'
os.system(cmd)
#No duplicqte elements in the sets
my_ip = ['192.168.1.1','192.168.1.2','192.168.1.3','192.168.1.1']
print(my_ip)
set_ip = set(my_ip)
print(set_ip)
print('-' * 80)
set_ip2 = {'8.8.8.4','8.8.8.8','192.168.1.2'}
union = set_ip | set_ip2
print(union)
intersection = set_ip & set_ip2
print(intersection)
set_ip.union(set_ip2)
set_ip.intersection(set_ip2)
print('-' * 80)
print(set_ip - set_ip2) # Unique elements in set 1
set_ip.difference(set_ip2)
print('-' * 80)
#print(set_ip ^ set_ip2)#Give only things that are not common in both set
print(set_ip.symmetric_difference(set_ip2))

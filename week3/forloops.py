some_list = ['192.168.1.1','192.168.1.2','192.168.1.3','10.1.1.1','10.1.1.1.2']
ip_list = some_list
print(str(len(ip_list)))
for ip in ip_list:
     print('The ip adddress is ')
     print(ip)
#Enumerate returns tuples with indexes and corresponding values
for ip in enumerate(ip_list):
    print('The ' + str(ip[0]+1) +' ip adddress is ' + ip[1])
    print (ip)
print(ip)
var1,var2 = ip
print(var1)
print(var2)
#Another way to write this and DONT TRY TO MODIFY IN LOOP OVER
for index, ip in enumerate(ip_list):
    print(index)
    print(ip)
    print('-' * 80)
#Break
for ip in ip_list:
     print('The ip address is ')
     print(ip)
     if ip=='10.1.1.1':
         break
print('-' * 80)
print('Behavior during for loop and continue statement')
for ip in ip_list:
    print('hello')
    if ip == '10.1.1.1': #does print 10.1.1.1
        continue #Goes back to the loop
    print(ip)

for ip in ip_list:
    pass
ip_list2 = ['8.8.8.8','8.8.8.4']
for ip in ip_list:
    for ip2 in ip_list2:
        print(ip2)
print('-' * 80)
i=0
for index1,ip1 in enumerate(ip_list):
    for index2,ip2 in enumerate(ip_list2):
        i = i+1
        print("Loop " + str(i))
print(list(range(10)))
for my_var in range(10):
    print(my_var)
print(list(range(3,10)))
print('10.1.1.2' in some_list)
print('10.1.1.1' in some_list)

some_list = ['8.8.8.8','192.168.1.1','172.16.20.1','10.1.1.1']
for ip in some_list:
    print(ip)
    if ip == '172.16.20.2': #Can be use to track a flag
        break
else:
    print('Hit the else clause')

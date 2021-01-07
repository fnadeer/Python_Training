Houston_dat = ['192.168.1.1','192.168.1.2','192.168.1.3','192.168.1.4','192.168.1.5','192.168.1.6','192.168.1.7','192.168.1.8','192.168.1.1','192.168.1.2']
Atlanta_dat = ['10.0.0.1','10.0.0.2','10.0.0.3','10.0.0.4','10.0.0.5','10.0.0.6','192.168.1.3','192.168.1.4']
Chicago_dat =['10.0.0.3','10.0.0.4','192.168.1.4','192.168.1.5','172.16.2.1','172.16.2.2','172.16.2.3','172.16.2.4']
Houston_dat = set(Houston_dat)
Atlanta_dat = set(Atlanta_dat)
Chicago_dat = set(Chicago_dat)
k = Houston_dat.intersection(Atlanta_dat)
print(k)
l = Houston_dat & Atlanta_dat & Chicago_dat
print(l)
m = (Chicago_dat-Atlanta_dat)-Houston_dat
print(m)

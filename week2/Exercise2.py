ip_addr = ["192.168.1.1","192.168.1.2","192.168.1.3","192.168.1.4","192.168.1.5"]
ip_addr.append("192.168.1.6")
ip_addr.extend(["192.168.1.7","192.168.1.8"])
ip_addr = ip_addr + ["192.168.1.9","192.168.1.10"] #Concatenate
print(ip_addr)
print("The last ip ip address is" + ip_addr[0] + " and the last is " + ip_addr[-1] )
ip_addr.pop(0)
ip_addr.pop()
ip_addr[0] = "2.2.2.2"
print(ip_addr)

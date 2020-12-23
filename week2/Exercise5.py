with open("show_ip_bgp_summ.txt") as f:
    output = f.readlines()
first_ln = output[0]
last_ln = output[-1]
first_ln = first_ln.split()
print("The AS number is",first_ln[-1])
last_ln = last_ln.split()
print("The peer IP address is",last_ln[0])

import os
cmd = 'clear'
os.system(cmd)
net_device = {'ip_addr2': '192.168.1.2', 'ip_addr': '192.168.1.1', 'Vendor': 'Cisco', 'Device Type': 'ios', 'Gateway': '192.168.1.3'}
#Graceful Exception handling
"""try:
    print("Statement Before")
    print(net_device['model'])
    print("Statement After")
except KeyError:
    print("Caught Exception")"""

#Catch and re-raise the Exception
"""try:
    print(net_device['Model'])
except KeyError:
    print("Caught Exception, re-raise")
    raise
print("After exception")""" #This wont be executed in re-raise

#Catch the Exception and retrieve info about it
"""try:
    print(net_device['Model'])
except KeyError as e:
    print(e.__class__)
    print(str(e))
    print("Caught Exception, printed info")"""


#Catch multiple exceptions
my_list = []
"""try:
    my_list[0]
    net_device['Model']
except(KeyError, IndexError):
    print("Handled multiple exceptions")

try:
    my_list[0]
    net_device['Model']
except(KeyError):
    print("Handled KeyError")
except(IndexError):
    print("Handled IndexError")"""

#Add a finally clause
"""try:
    net_device['Model']
except(KeyError):
    print("Handled KeyError")
finally:
    print("Finally is always executed whether exception or not")"""

#Handle any exception (Be careful!)
try:
    net_device['Model']
except Exception:
    print("Model not found")

import re
with open("show_version.txt") as f:
    output = f.read()
os_ver = re.search(r"^Cisco.*, Version (\S+), .*$", output, flags = re.M).group(1)
ser_num = re.search(r"Processor board ID (\w+)$", output, flags = re.M).group(1)
conf_reg = re.search(r"Configuration register is (\S+)$", output, flags = re.M).group(1)
print(f"OS Version: {os_ver}")
print(f"Serial number: {ser_num}")
print(f"Config Register: {conf_reg}")

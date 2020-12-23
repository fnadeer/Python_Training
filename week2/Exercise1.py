"""f = open("show_version.txt")
output = f.read()
print(output)
print(type(output))
f.close"""
with open("show_version.txt") as f:
    output = f.readlines()
print(output)
print(type(output))

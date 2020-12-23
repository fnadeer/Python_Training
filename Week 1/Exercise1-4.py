show_version = '*0           CISCO881-SEC-K9             FTX0000038X'
show_version = show_version.strip()
print(show_version)
ext = show_version.split()
print(f"The model is {ext[1]} and the serial number is {ext[2]}")
if 'cisco' in ext[1].lower():
    print("Yes the model is Cisco")
print("The word 'Cisco'is contained in the model: {}".format('cisco' in ext[1].lower()))
print("The '881'is contained in the model: {}".format('881' in ext[2]))

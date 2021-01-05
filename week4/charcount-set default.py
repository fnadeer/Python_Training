with open("show_version.txt") as f:
    output = f.read()
count = {}
for character in output:
    count.setdefault(character,0)
    count[character] = count[character] + 1
temp_value = 0
for k, v in count.items():
    if v > temp_value:
        temp_value = v
        temp_key = k
print(count)
print("Max occurance is " + str(temp_key) + " with " + str(temp_value) + " occurances")

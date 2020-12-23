f = open("test.txt")
print(f)
output = f.read()
print(output.splitlines())
f.seek(0)
print()
print ('-' * 80)
#output = f.readline()
output_list = f.readlines()
print(output_list)
#f.seek(0) #to go bqck to the beginning of the file
f.close() # to close the file,best practise
with open("test.txt") as f:
    output = f.read() #python automatically close this and doesn't need a close statement
print(output)
f = open("writetest.txt",mode="w") #This writing is destructive
f.write("Hello i am trying to write new content into it\n")
f.write("Hello i am trying to write new content into it\n")
f.write("Hello i am trying to write new content into it\n")
f.flush()
f = open("writetest.txt",mode="w")
f.write("New Line")
f.close()
f = open("writetest.txt",mode = "a")
f.write("\nTrying to append the contents of the file")
f.close()

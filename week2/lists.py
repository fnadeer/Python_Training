f = open("show_version.txt")
output = f.readlines()
print(type(output))
print(len(output))
output_slice = output[0:5]
#print(output[:]) prints all the elements of the list
print(type(output_slice))
print(output_slice)
my_list = []
my_list = ['Whatever', 22, 'hellyea']
print(len(my_list))
my_list.append("Appended item")
my_list += [2,3,4]
my_list.extend([2,'hello',72,31,'hello','Bonjour'])
print(my_list)
print(my_list.pop()) #Removes the last item from the list
my_list.pop(0)
print(my_list)
print(my_list.count('hello')) #Count the number of hellos
print(my_list.index('hello')) #print the first index of hello
print(my_list.remove('hello')) #Removes rhe first hello
print(my_list)

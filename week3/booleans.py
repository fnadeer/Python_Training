a = True
print(type(a))
b = False
print ( a and b)
print(a or b)
print(10 > 2)
print((10 > 2) or (7==7))
if ((10 > 2) or (7==7)):
    print("Hello")
a = 'whatever'
print(bool(a))
b= ''
print(bool(b))
c=0
print(bool(c))
print(bool([]))
my_val = 10
a= 'whatever' if my_val > 2 else 'something' #Ternary operator
print(a)
a = None
print(type(a))
print(bool(a))

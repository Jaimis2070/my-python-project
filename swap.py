a = int(input("Enter the number"))
b = int(input("Enter the number"))

print('~~~~~~~~~~~~~~before swap~~~~~~~~~~~~~')
print(a)
print(b)
a = a + b
b = a - b
a = a - b
print('~~~~~~~~~~~~~~~after swap~~~~~~~~~~~~~')
print(a)
print(b)
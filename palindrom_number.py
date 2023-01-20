n = int(input('Enter the number '))
c = 0
while n>0:
    rev = n % 10
    c = c * 10 + rev
    n = n//10
print(c)

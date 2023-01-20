n = int(input("Enter the number :"))
temp = n
sum = 0
while temp > 0:
        rev = temp % 10
        sum = sum * 10 + rev
        temp = temp // 10
if n == sum:
    print(n,"This number is palindrom number")
else:
    print(n,"This number is not palindrom number")
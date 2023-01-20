n = int(input("Enter the number :"))
temp = n
sum = 0
while temp > 0:
        rev = temp % 10
        sum = sum+rev**3
        temp = temp // 10
if n == sum:
    print(n,"This number is armstrong number")
else:
    print(n,"This number is not armstorng number")
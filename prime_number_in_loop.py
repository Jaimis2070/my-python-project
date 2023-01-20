a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
for number in range(a,b+1):
    if number>1:
        for i in range(2,number):
            if number%2==0:
                break
        else:
            print(number)

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))
num = b
while (num >= a):
    if (num % c) == 0:
        print(num)
        num -= 1
    else:
        num -= 1
        continue
    

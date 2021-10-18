a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))
for i in range (b, a - 1, -1):
    if (i % c) == 0:
        print(i)


n = int(input("Enter N: "))
sum = 0
if (n < 1):
    print("ERROR")
else:
    for i in range (1, n + 1):
        sum += i**2
    print("The sum is:", sum)

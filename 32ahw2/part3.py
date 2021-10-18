one = int(input("Enter first number: "))
two = int(input("Enter second number: "))
three = int(input("Enter third number: "))
if (one <= two):
    if (one <= three):
        print("Lowest number:", one)
elif (two <= one):
    if(two <= three):
        print("Lowest number:", two)
elif (three <= one):
    if (three <= two):
        print("Lowest number:", three)

dimes = int(input("How many dimes: "))
nickels = int(input("How many nickels: "))
pennies = int(input("How many pennies: "))
total = dimes * 0.1 + nickels * 0.05 + pennies * 0.01
print("You have:", round(total, 2))

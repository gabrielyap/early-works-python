firstName = str(input("Enter the first name: "))
secondName = str(input("Enter the second name: "))
if firstName < secondName:
    print("Say hello to ", firstName, " and ", secondName, ".", sep = "")
else:
    print("Say hello to ", secondName, " and ", firstName, ".", sep = "")

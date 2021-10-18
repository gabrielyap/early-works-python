a = str(input("Enter the first string: "))
b = str(input("Enter the second string: "))
c = str(input("Enter the third string: "))

if (a < b and a < c):
    if (b < c):
        print("In order, the strings are ", a, ", ", b, ", and ", c, ".", sep = "")
    if (c < b):
        print("In order, the strings are ", a, ", ", c, ", and ", b, ".", sep = "")
if (b < a and b < c):
    if (a < c):
        print("In order, the strings are ", b, ", ", a, ", and ", c, ".", sep = "")
    if (c < a):
        print("In order, the strings are ", b, ", ", c, ", and ", a, ".", sep = "")
if (c < a and c < b):
    if (a < b):
        print("In order, the strings are ", c, ", ", a, ", and ", b, ".", sep = "")
    if (b < a):
        print("In order, the strings are ", c, ", ", b, ", and ", a, ".", sep = "")

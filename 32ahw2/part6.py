first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
if (first and second != 0):
    if (first < 0 and second < 0) or (first > 0 and second > 0):
        print("Product is positive")
    elif (first > 0 and second < 0) or (first < 0 and second > 0):
        print("Product is negative")
else:
    print("Product is zero")
    
    
                  

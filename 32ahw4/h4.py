def is_even(n): #1
    if (n % 2 == 0):
        return True
    elif (n % 2 != 0):
        return False

def is_triangle(a, b, c): #2
    if (a + b < c or b + c < a or c + a < b):
        return False
    else:
        return True

def try_triangle(): #2.5
    len1 = int(input("Enter first length: "))
    len2 = int(input("Enter second length: "))
    len3 = int(input("Enter third length: "))
    return is_triangle(len1, len2, len3)
        
def has_consecutive(s): #3
    result = False
    for i in range((len(s) - 1)):
        if s[i + 1] == s[i]:
            result = True
    return result

def ess(s1, s2): #4
    sNew = ""
    sNew += (str(len(s1)) + " " + s1 + s2)
    return sNew

def dess(s , n): #4.5
    if (n != 1 and n != 2):
        return "ERROR"
    num = s[0]
    if (n == 1):
        return s[2 : (int(num) + 2)]
    if (n == 2):
        return s[int(num) + 2 :]

def bitwise_or(one, two): #5
    if (len(one) != len(two)):
        return "ERROR"
    sNew = ""
    for c in range(len(one)):
        if (one[c] == "1" or two[c] == "1"):
            sNew += "1"
        else:
            sNew += "0"
    return sNew
#record every third in a string, if all in string equal eachother true
def every_third_equal(s): #6
    new = s[2 : len(s) : 3]
    if len(new) == 1:
        return True
    for i in range(0, len(new) - 1):
        if new[i] == new[i + 1]:
            key = True
        else:
            return False
    return key
        
def max_length(s1, s2, s3): #7
    if (len(s1) >= len(s2) and len(s1) >= len(s3)):
        return len(s1)
    if (len(s2) >= len(s1) and len(s2) >= len(s3)):
        return len(s2)
    if (len(s3) >= len(s1) and len(s3) >= len(s2)):
        return len(s3)
            
def interleave(a, b, c):
    big = max_length(a, b, c)
    if len(a) < big:
        for i in range(big - len(a)):
            a += " "
    if len(b) < big:
        for i in range(big - len(b)):
            b += " "
    if len(c) < big:
        for i in range(big - len(c)):
            c += " "
    new = ""
    for i in range(big):
        new += a[i] + b[i] + c[i]
    return new

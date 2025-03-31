def reverseString(s):

    if len(s) == 1:
        return s[0]
    
    firstChar = s[0]

    return reverseString(s[1:]) + firstChar

s = input("enter your strings:")
print(reverseString(s))
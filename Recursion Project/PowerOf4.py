n = int(input("enter the number"))


def checkIFPower(n):
    if n <= 0:
        return False
    
    if n <= 1:
        return True
    
    if n % 4 == 0:
        return checkIFPower(n // 4)
    return False

if checkIFPower(n):
    print("Power Of 4")

else:
    print("not power of 4")


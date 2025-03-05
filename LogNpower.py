def computePower(x,y):

    result = 1 

    while y > 0:
        if (y % 2 == 0):
            x = x * x 
            x >>= 1
        else:
            result = result * x
            y = y - 1

    return result



print(computePower(2,5))
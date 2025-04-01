def ways(stairs):

    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    
    twoSteps = 0
    oneSteps = 0

    if stairs >= 2:
        twoSteps = ways(stairs - 2)
    
    oneSteps = ways(stairs - 1)

    return twoSteps + oneSteps

stair = int(input("enter a value:"))
print(ways(stair))
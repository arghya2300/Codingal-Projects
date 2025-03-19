import math

def printPowerSet(input_set, set_size):

    power_set_size =  int(math.pow(2,set_size))

    for outer in range(power_set_size):
        for inner in range(set_size):
            if (outer& (1 << inner)) > 0:
                print(input_set[inner], end=" ")
        print("")

size = int(input("Enter array size: "))

input_set = []

for i in range(size):
    n =  int(input("Enter element: "))
    input_set.append(n)

print("Power Set:")
printPowerSet(input_set,len(input_set))

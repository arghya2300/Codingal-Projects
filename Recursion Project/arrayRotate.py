def rotate(a,a_size):
    temp = a[0]
    for i in range(a_size - 1):
        a[i] = a[i + 1]
    a[a_size - 1] = temp


def rotation(a,n,a_size):
    for i in range(n):
        rotate(a, a_size)


def printArray(a,a_size):
    for i in range(a_size):
        print("%d" % a[i], end=" ")
    print("\n")

a = [10, 20 ,30, 40 , 50]
print("original array:")
printArray(a,len(a))

rotation(a, 2, len(a))

print("Array after 2 left rotations:")
printArray(a,len(a))
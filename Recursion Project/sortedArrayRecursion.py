def checkSorted(a):

    length = len(a)

    if length == 1 or length == 0:
        return True
    
    return a[0] <= a[1] and checkSorted(a[1:])


a = [1, 2, 3, 5, 6, 8, 2]


if checkSorted(a):
    print("\nYes, the given array is sorted")

else:
    print("\nNo, the given array is not sorted")

    
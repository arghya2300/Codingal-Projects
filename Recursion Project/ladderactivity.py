def leaders(a, a_size):
 
    currentmax = a[a_size - 1]
    print(currentmax)

    for i in range(a_size - 2, -1, -1):
        if currentmax < a[i]:
            print(a[i])
            currentmax = a[i]

# Example usage
a = [16, 17, 4, 3, 5]
print("Leaders in the array:")
leaders(a, len(a))

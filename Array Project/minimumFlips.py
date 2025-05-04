def print_min_flips(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            if arr[i] != arr[0]:
                print(f"From {i} to ", end="")
            else:
                print(f"{i - 1}")
    if arr[n - 1] != arr[0]:
        print(f"{n - 1}")

arr = [0, 1, 1, 0, 0, 0, 1, 1]
print_min_flips(arr)

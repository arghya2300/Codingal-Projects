def find_missing_number(arr):
    n = len(arr) + 1  
    total = n * (n + 1) // 2  
    actual_sum = sum(arr)
    missing_number = total - actual_sum
    return missing_number


arr = [1, 4, 3, 2, 6]
print("Missing number is:", find_missing_number(arr))

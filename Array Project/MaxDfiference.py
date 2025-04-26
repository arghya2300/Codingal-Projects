def max_difference(arr):
    min_element = arr[0]
    max_diff = 0

    for num in arr:
        if num < min_element:
            min_element = num
        else:
            max_diff = max(max_diff, num - min_element)

    return max_diff

a = [4, 5, 234, 2, 6, 82, 234, 5234]
print("Maximum Difference:", max_difference(a))

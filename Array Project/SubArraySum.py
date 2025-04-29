def maxSubArraySum(a,a_size):
    max_sum = -99999999
    cmax = 0
    
    for i in range(0,a_size):
        cmax = cmax + a[i]

        if max_sum < cmax:
            max_sum = cmax

        if cmax < 0:
            cmax = 0

    return max_sum

array = [1, 2, 3, -4, 5, -22, -4, 25, 2, -9]
print(maxSubArraySum(array, len(array)))


def calculateProfits(arr,arr_size):
    profit = 0
    for i in range(1,arr_size):
        if arr[i] > arr[i - 1]:
            profit = profit + arr[i] - arr[i - 1]
    return profit


price = [100, 180, 260, 310, 40, 535, 695]

profit = calculateProfits(price,len(price))
print("max profit:", profit)
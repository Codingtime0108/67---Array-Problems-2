def calculateProfits(arr,arr_size):

    profit = 0
    for i in range(1, arr_size):

        if arr[i]>arr[i-1]:

            profit += arr[i] - arr[i-1]
    return profit
prices = [128,984,762,643,567,891,234,456]

profit = calculateProfits(prices, len(prices))
print("Max profit: ",profit)
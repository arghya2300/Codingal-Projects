def count_ways(amount, coins, index=0):
    if amount == 0:
        return 1  
    if amount < 0 or index >= len(coins):
        return 0 

    include = count_ways(amount - coins[index], coins, index)

    exclude = count_ways(amount, coins, index + 1)

    return include + exclude


def find_ways(amount):
    coins = [500, 100, 10, 5, 1]
    return count_ways(amount, coins)

n = int(input("Enter the amount: "))
print("Ways to make change:", find_ways(n))

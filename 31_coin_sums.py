"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

1*£1 + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p

How many different ways can £2 be made using any number of coins?
"""

def count_ways_to_make_amount(amount, coins):
    ways = [0] * (amount + 1)
    ways[0] = 1
    
    for coin in coins:
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]
            
    return ways[amount]

# Define the coin denominations and target amount
coins = [1, 2, 5, 10, 20, 50, 100, 200]
target_amount = 200

# Calculate the number of ways to make £2
result = count_ways_to_make_amount(target_amount, coins)
print(f"The number of ways to make £2 is: {result}")
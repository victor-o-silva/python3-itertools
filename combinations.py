import itertools

"""
    You have three $20 dollar bills, five $10 dollar bills, two $5 dollar bills, and five $1 dollar bills.
    How many ways can you make change for a $100 dollar bill?
"""


bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
makes_100 = set()
for size in range(1, len(bills) + 1):
    for combination in itertools.combinations(bills, size):
        if sum(combination) == 100:
            makes_100.add(combination)

print(f'makes_100 with pre-set bills: {makes_100}')


"""
    How many ways are there to make change for a $100 bill using any number of $50, $20, $10, $5, and $1 dollar bills?
"""

bills = [50, 20, 10, 5, 1]
max_count = 100 // min(bills)
makes_100 = set()
for size in range(1, max_count + 1):
    # print(f'Iteration with size={size}')
    for combination in itertools.combinations_with_replacement(bills, size):
        if sum(combination) == 100:
            makes_100.add(combination)

print(f'makes_100 with any number of bills: {makes_100}')

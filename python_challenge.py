import math

sale_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3,
    15,
    45
]

sorted_list = sorted(sale_prices)

list_length = len(sorted_list)-1

middle = (list_length / 2)

median = sorted_list[int(middle)]

print(median)
print(sorted_list)

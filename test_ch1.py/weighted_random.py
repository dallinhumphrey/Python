import random

dictionary = {
 "1" : "Winner",
 "2" : "Break Even",
 "3" : "You lost"
}

weighted_dictionary = ['winner'] * 1 + ['break_even'] * 2 + ['loser'] * 3

random.choice(weighted_dictionary)


print(random.choice(weighted_dictionary))
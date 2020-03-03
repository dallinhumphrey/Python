# def full_name(first, middle, last):
#     return f'{first} {middle} {last}'
#
#
# insult = full_name('smelly', 'rat', 'turd')
#
#
# def greeting(name):
#     print(f'Hi {name}!')
#
#
# greeting(insult)
#

# print(random.randint(0, 10))


def greeting(time_of_day, *args):
    print(f"Hi {' '.join(args)}, I hope that you are having a good {time_of_day}")


greeting('Morning', 'Dallin', 'Humphrey')
greeting('Afternoon', 'Dallin', 'Scott', 'Humphrey')

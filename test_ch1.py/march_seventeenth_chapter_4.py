twoRivers = ['Rand', 'Perrin', 'Faile', 'Mat', 'Egwene', 'Nynaeve']


visit = ['new zealand', 'fuji', 'costa rica', 'bali', 'lake powell']

for character in twoRivers:
    print(character.title() + ", killed a trolloc!")
    print("I can't wait to see you do it again, " + character.title() + "\n")

print("Thank you everyone! That was a great show!")

pizzas = ['cheese', 'veggie', '4 cheese', 'pineapple']

for pizza in pizzas:
    print(f"""I love {pizza.title()} pizza!""")

print(f"""
Pizza is my favorite food in the whole world, and I think {pizzas[2]} is my favorite. {pizzas[-1]} is super close too!
""")

numbers = list(range(1, 11, 2))
print(numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

house_members = ['kort', 'dallin', 'lincoln', 'lily']

for house_member in house_members:

    print(f"""{house_member.title()} is super cool \n""")
print(f"""We have fun here""")

squares = []
for value in range(1, 11, 2):
    squares.append(value**2)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

numbers = range(3, 31, 3)
for numb in numbers:
    print(numb)


numbers = list(range(3, 31, 3))
print(numbers)

for numb in numbers:
    numb = list(range(3, 31, 3))
print(numb)

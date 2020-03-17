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

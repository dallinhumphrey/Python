bicycles = ['huffy', 'trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

twoRivers = ['Rand', 'Perin', 'Mat', 'egwene', 'Nynaeve']
message = f"""{twoRivers[0]} ate with {twoRivers[1]} and {twoRivers[2]}. """
print(message)

message_two = f'''{twoRivers[3].title()} and {twoRivers[-1].title()} don't get along great and argue about {twoRivers[0]}.'''
print(message_two)

motorcycles = ['suzuki', 'honda', 'yamaha']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles.append('harley')
print(motorcycles)

motorcycles_two = []
motorcycles_two.append('suzuki')
motorcycles_two.append('honda')
motorcycles_two.append('yamaha')
motorcycles_two.append('ducati')

print(motorcycles_two)

menu = []
menu.append('eggs')
menu.append('toast')
menu.append('hash browns')
menu.append('pancakes')
menu.append('waffles')
menu.append('french toast')

menu.insert(3, 'cookies')
print(menu)

popped_menu = menu.pop()
print(menu)
print(popped_menu)
popped_menu = menu.pop()
print(popped_menu)

print(menu)
print(popped_menu)

last_eaten = f'''The last thing I ate for breakfast was {popped_menu}'''
print(last_eaten)

last_eaten = f'''The first thing I ate for breakfast was {menu.pop(0)}'''
print(last_eaten)

menu.insert(4, 'chocolate chip cookies')
menu.insert(2, 'snow cones')
menu.insert(5, 'candy corn')
print(menu)

twoRivers = ['Rand', 'Perrin', 'Mat', 'Egwene', 'Nynaeve']

twoRivers.insert(2, 'Faile')


print("OG list")
print(twoRivers)

print("Temp sorted list")
print(sorted(twoRivers))

print("back to normal")
print(twoRivers)

print("reverse order isn't in alphabetical order, and is perm unless it's reversed again.")
twoRivers.reverse()
print(twoRivers)

print("back to original order.")
twoRivers.reverse()
print(twoRivers)

twoRivers = ['Rand', 'Perrin', 'Faile', 'Mat', 'Egwene', 'Nynaeve']


visit = ['new zealand', 'fuji', 'costa rica', 'bali', 'lake powell']

print(visit)
print(sorted(visit))
print(visit)

visit.reverse()
print(visit)

visit.reverse()
print(visit)

visit.sort(reverse=True)
print(visit)

two_rivers_dinner = len(twoRivers)
print(f""" There will be {two_rivers_dinner} guests at tonights dinner""")

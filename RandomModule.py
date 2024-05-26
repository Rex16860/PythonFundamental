import random as rd
from random import *

print(rd.random)
print(randint(1, 5))
print(randrange(10, 101, 10))
print(random())
print([rd.randint(50, 100)] * 8)
print(rd.uniform(2, 3))
print()

animals = ['\N{tiger}', '\N{snake}', '\N{eagle}', '\N{owl}']
print(type(animals))
print(animals)
rd.shuffle(animals)
print(animals)
print(animals[1])

heroes = ['Chainsawman', 'Agni', 'Itadori', 'L']
villains = ['Johan', 'Judah', 'Lelouch', 'Light']
rd.shuffle(heroes)
rd.shuffle(villains)

for i in range(0, len(villains)):
    print(heroes[i], 'Vs', villains[i])

menu = ['noodles', 'cashew with tofu', 'coconut rice']
print(rd.choice(menu))

# probabilities = [0.25] * 4
probabilities = [0.9, 0.1, 0.1, 0.3]
students = ['Ren', 'Michel', 'Dwayn', 'Jessie']
print(rd.choices(students, probabilities, k=10))
print(rd.sample(range(10, 40), k=3))
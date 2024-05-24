d1 = {}
print(type(d1))
d1["a"] = 11
d1["b"] = 14
d1["c"] = 19

print(d1)

weapons = {'Sniper': "$399", 'Pistol': "$100"}
d1.update(weapons)
d1["a"] = 120
d1["d"] = 320
print(d1)

d1.pop('a')
print((d1))

print(list(d1.keys())[2:4])

print(d1.items())
print(list(d1.items()))
print(dict(list(d1.items())))

menu = [("hambaga", 2.5), ("cheese", 1.9)]
print(dict(menu))

maze = {'k1': d1, 'k2': [10, 20, 30], 'k3': ('tuple!', [1, 2, {'k4': ['a', 'b', 'catch me!']}])}
print(maze)

print(tuple((list(maze.values())[2][1][2]).values())[0][2])
print('got you nyahaha')

print(maze['k3'][1][2]['k4'][2])

weapon = dict(name='bow', attack=15, durability=100)
print(weapon['attack'])
print(list(weapon.items())[0::2])
print(weapon['name'])
weapon['attack'] = 20
print(weapon)
print(len(weapon))

weapon2 = {
    'name': 'sword',
    'attack': 20,
    'durability': 120
}

print(weapon2['name'])

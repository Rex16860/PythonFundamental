print(list(range(0, 22, 4)))
print(list(range(-100, 50, 10)))

nest = [[1, 2, 3], [5, 6, 7]]
new = [list(range(5)), list(range(5, 10))]

print(nest + new)

n = list(range(70, 40, -10))
n.append(10)

n.clear()
n. append([38, 20, 22, 11])
print(n)
n = n[0]
print(n)

n.sort()
print(n)

n.insert(0, 9)
print(n)

n.pop()
print(n)

weapons = ["bow", "sword", "knive", "spear"]
weapons[2] = "dagger"
print(weapons)

weapons.append(n)
print(weapons)

weapons[4].insert(len(weapons[4]) - 1, ["Hello"])
print(weapons)

print(weapons[4][3][0])

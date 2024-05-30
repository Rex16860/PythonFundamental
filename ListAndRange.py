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

mangas = ['Fire Punch', 'Good Bye Eri', 'Look Back']
print('\n{0}, {1}, {2}'.format(mangas[0], mangas[1], mangas[2]))

print(f'my favourite is {mangas[0]}')

for manga in mangas:
    if manga == 'Fire Punch':
        print('\n' + manga + '(This is my favourite one)')
    else:
        print(manga)

for i in range(len(mangas)):
    if mangas[i] == 'Fire Punch':
        print('\n' + mangas[i] + '(This is my favourite one)')
    elif mangas[i] == mangas[len(mangas) - 1]:
        print(mangas[i] + '\n')
    else:
        print(mangas[i])

mangas.append('Chainsawman')
mangas.append('JJK')
print(mangas)
completed = []
for i in range(len(mangas)):
    if i > 2:
        None
    else:
        completed.append(mangas.pop(i))

print('completed: ')
print(completed)
print('\n')
print(mangas)
addList = input('Add manga list: ')

if addList.title() in mangas:
    print('The manga is already exist in your list')
    var = False

else:
    print('added')
    mangas.append(addList.title())
    print(mangas)

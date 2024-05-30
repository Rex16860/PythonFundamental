mangas = ['Fire Punch', 'Good Bye Eri', 'Look Back', 'Chainsawman', 'JJK', "The GigaChad Dad's hero"]
print(mangas)
print('\n')

# newMangas = mangas[:]
# del mangas
# print(newMangas)

newMangas = []
for manga in mangas:
    newMangas.append(manga)

del mangas
print(newMangas)
print('\n')

mangas = ['Fire Punch', 'Good Bye Eri', 'Look Back', 'Chainsawman', 'JJK', "The GigaChad Dad's hero"]
print(mangas)
print('\n')

print('even: ')
newMangas = mangas[1::2]
print(newMangas)
print('\n')

print('Odd: ')
newMangas = mangas[0::2]
print(newMangas)
print('\n')

mangas = ['Fire Punch', 'Good Bye Eri', 'Look Back', 'Chainsawman', 'JJK', "The GigaChad Dad's hero"]
print(mangas)
print('\n')

Even = []
Odd = []
for i in range(len(mangas)):
    if i % 2 == 0:
        Even.append(mangas[i])
    elif i % 2 == 1:
        Odd.append(mangas[i])

print(Even)
print('\n')
print(Odd)

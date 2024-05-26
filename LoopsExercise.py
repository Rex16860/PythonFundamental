# E1
ns = list(range(0, 110, 10))
f = []
i = 0

while i < len(ns):
    s = ns[i] * 2.5
    if s % 2 == 0:
        f.append(int(s))
    i += 1

print(f)

# E6
d1 = {'k1': [20, 30, 40], 'k2': [1000, 2000, 3000]}

for i in range(3):
    print('total = ', d1['k1'][i] + d1['k2'][i])
    if i == 2:
        print('End loop')

rep = ['joe', 'mike', 'joi', 'luv', 'deckard', 'wallace', 'rachel']

for i in rep:
    if len(i) == 6 or len(i) == 3:
        print(i, 'is a replicant')
    else:
        print(i, 'is not a replicant')

# E2
print('Human')
for r in range(2):
    k = 0
    while k < 8:
        if k % 2 == 0:
            print('Question')
        elif 3 < k < 7:
            print('Cell')
        elif k == 3:
            print('Interlinked')
        else:
            print('cell within cells')
        k += 1
print('time to finish')

# E3
y = 0
x = 0
print('start')
while y < 8:
    for x in range(4, 9):
        print('y =', y)
        print('________')
        print('x is equal to', x)
        print('________')
        y += 2
        x += 1
print('end')

# 4
students = ['natAlie', 'm', 'Fa ye', ' Callum', 'Tara']

names = []
for i in students:
    if len(i) > 1:
        s = i.upper().replace(' ', '')
        names.append(s)
print(tuple(names))

# 5
prices = {'popcorn': 5, 'soda': 2, 'veggie burger': 7}
total = []

v = 0
while v < 2:
    n1 = input('would u like popcorn with the film?')
    if n1 == 'no':
        var = None
    elif n1 == 'quit':
        print('enjoy the film')
        break
    else:
        total.append(prices['popcorn'])

    n2 = input('would u like soda with the film?')
    if n2 == 'no':
        var = None
    elif n2 == 'quit':
        print('enjoy the film')
        break
    else:
        total.append(prices['soda'])

    n3 = input('would u like a veggie burger?')
    if n3 == 'no':
        var = None
    elif n3 == 'quit':
        print('enjoy the film')
        break
    else:
        total.append(prices['veggie burger'])

    v += 1
    print('That will be $', str(sum(total)))
    print('enjoy the film')
    break

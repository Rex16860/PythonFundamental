
for hello in range(1, 11, 2):
    print(hello)

cats = ['tiger', 'lion', 'jaguar', 'leopard']
for cat in cats:
    print(cat)

for num in range(1, 5):
    print(num, num + 1, num + 2)

nest1 = [10, 20, 30], [3.5, 4.5, 5.5], ['sword', 'hammer', 'shield']

for i in range(3):
    print(nest1[i])

weapons = []
for i in range(3):
    res = nest1[0][i] + nest1[1][i]

    print(nest1[2][i].capitalize() + ': power level =', res)

for i in range(3):
    s = nest1[2][i].capitalize() + ': power level = ' + str(nest1[0][i] + nest1[1][i])
    weapons.append(s)
print(weapons[1])

for i in range(1, 10):
    print('{} * {} = {}'.format(i, i + 1, (i * (i + 1))))

for k in range(1, 8):
    print('%.2f * %.2f = %.2f' % (k, k, (k * k)))

tupl = ((10, 20, 30), ('a', 'b', 'c'), (200, 400, 800))
# Tuple Unpacking
for i in range(3):
    for x, y, z in tupl:
        print(x, y, z)

cakes = ['chocolate', 'lemon', 'carrot', 'vanilla']

d1 = {'k1': tuple(cakes), 'k2': list(range(10, 41, 10))}

print(d1['k2'])

for d in d1['k1']:
    print(d)
    for d2 in d1['k2']:
        print(d2)

for x in d1:
    for i in range(4):
        print(x, ' : ', d1[x][i])

print(cats)
endangered = ['series', 'critical', 'vary critical', 'stable']

for c in range(4):
    print(cats[c].capitalize(), '\n Level: \n', endangered[c].upper())

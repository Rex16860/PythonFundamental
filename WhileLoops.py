x = 50
while x <= 100:
    print(x)
    x += 10

n = 1
while n < 20:
    print('the multiplication is: ', n)
    n *= 2

div = 1000
while div > 10:
    print('the divition is:', round(div), 2)
    div /= 3

p = 1
while p < 8:
    print('{} + {} = {}'. format(p, p, (p + p)))
    p += 1

a = 1
while a < 8:
    print('%.2f * %.2f = %.2f' % (a, a, (a * a)))
    a += 1

p = 1
o = 1
while p < 15 and 0 < 15:
    print('%i / %.2f = %i' % (p, o, (p / o)))
    p += 1
    o += 1

n = 5
cake = 10
while n < 12:
    while cake < 17:
        print('{0} + {1} + {0} = {2}'.format(n, cake, n, n + cake))
        cake += 1
        n += 1

lang = ['PHP', 'Peython', 'Java', 'Javascript', 'Go', 'css', 'Typescript', 'HTML', 'R', 'c', 'c++', 'c#']
x = 1
while x < len(lang):
    print(lang[x])
    x += 1

a = 1
b = 1
while a < 5:
    while b < 5:
        print('{} + {} = {}'.format(a, b, a + b))
        a += 1
        b += 1

for j in range(1, 5):
    for i in range(1, 5):
        print('{} + {} = {}'.format(j, i, j + i))

for t in range(1, 5):
    print('{} + {} = {}'.format(t, t, (t + t)))

n1 = 0
while n1 < 51:
    print('while n1 = ', n1)
    for g in [50, 80, 110]:
        res = n1 + g
        print(res)
    n1 += 10

x = 0
while x < 5:
    print('while x = ', x)
    for g in range(1, 6):
        res = x + g
        print(res)
    x += 2

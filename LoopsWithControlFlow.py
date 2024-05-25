for i in range(10):
    if i % 2 == 0:
        print('even number : ', i)
    else:
        print('odd number : ', i)

for i in range(10):
    if i == 4:
        print('fatastic four!')
    elif i == 7:
        print('nanatsu no '
              'taizai!')
    else:
        print(i)

x = 0
while x < 10:
    if x == 6:
        print('should I take a break?')
    elif x > 8:
        print('maybe not')
    else:
        print('because this language is cool!')
    x += 1

num = [10, 5, 20, 3, 100, 4, 7]
rad = [4, 1, 40, 3, 120, 5, 7]

x = 0
while x < len(num):
    if num[x] == rad[x]:
        print('equal'.upper())
    elif num[x] > rad[x]:
        print('GREATER')
    else:
        print('Less')
    x += 1

for x in range(len(num)):
    if num[x] == rad[x]:
        print('equal'.upper())
    elif num[x] > rad[x]:
        print('GREATER')
    else:
        print('Less')

animals = ['tiger', 'snake', 'eagle']

"""
while True:
    n = eval(input("Enter a number here : "))
    if n >= 3:
        print('keep looking')
    elif animals[n] == 'tiger':
        print('found a tiger')
    elif animals[n] == 'snake':
        print('found a snake')
    else:
        print('found an eagle')
"""
total = [list(range(11)), list(range(11, 21)), list(range(21, 31))]
print(total)

while True:
    v = eval(input('input a number here : '))

    if v in total[0]:
        print(v, 'in list one')
    elif v in total[1]:
        print(f'{v} in list two')
    elif v in total[2]:
        print(f'{v} in list three')
    elif v == 0.5:
        print('bye')
        break
    else:
        print(f'{v} not in any list')

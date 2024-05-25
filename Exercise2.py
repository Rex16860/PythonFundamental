# E1
"""d1 = {'k1': [1, 2, 3, (100, 300, 500)], 'k2': [4, 5, 6, ['phone', 'computer', 'robot']]}
v = eval((input('Enter a number: ')))

if v in d1['k1']:
    print('found you!')
    n = input('enter a number: ')
    # code
    if eval(n) in d1['k2'][:3]:
        print('found another one!')

        item = input('enter an item: ')

        if item in d1['k2'][3]:
            print('got a', item)
        else:
            print("can't find a", item)
    else:
        print("can't find anything!")
elif v in d1['k1'][3]:
    print("can't hide!")
else:
    print('where are ya?')"""

# E2
chooseDish = eval(input('Enter a number 0 t0 2: '))
pickSauce = eval(input('Enter a number 0 t0 2: '))

if chooseDish > 2 and pickSauce > 2 or chooseDish < 3 and pickSauce > 2 or chooseDish > 2 and pickSauce < 3:
    None
else:
    coockedPasta = ['hot', 'cold', 'over cooked'][chooseDish]
    sauce = ['spicy', 'sweet', 'savoury'][pickSauce]

    print(coockedPasta, sauce)

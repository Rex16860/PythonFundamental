import random

while True:
    luckyCoin = {'head', 'tail'}

    # Random index
    luckyCoinIndex = random.randrange(0, len(luckyCoin))

    # Put Random value
    coin = list(luckyCoin)[luckyCoinIndex]

    chooseCoin = input("Choose coin : ")

    if coin == 'head' and chooseCoin == 'head':
        print('Lucky')
    elif coin == 'tail' and chooseCoin == 'head':
        print('Uncanny')
    elif coin == 'tail' and chooseCoin == 'tail':
        print('Lucky')
    elif coin == 'head' and chooseCoin == 'tail':
        print('Uncanny')
    elif chooseCoin == 'x':
        break
    else:
        'error'

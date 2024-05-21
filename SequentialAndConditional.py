"""
Syntax semua bahasa pemrogramman ada 3, yaitu:
1. Squential : langkah berurutan.
2. Percabangan : melompat jika kondisi terpenuhi.
3. Perulangan : mengulangi perintah sampai kondisi terpenuhi
"""

# Sequential
print('Mumma : "Go to convenient store and buy 1 bottle milk. If there are eggs, buy 6 eggs"')
print('Bro : "Gotta go" ')
print('Bro arrived on the convinient store')

# Percabangan

import random

storeluck = random.randint(0, 1)
milkluck = random.randint(0, 1)
eggluck = random.randint(0, 1)
lucky = 0

if storeluck > 0:
    lucky = storeluck
    if milkluck > 0:
        lucky = lucky + milkluck
        if eggluck > 0:
            luck = lucky + eggluck
    if eggluck > 0:
        lucky = lucky + eggluck
else:
    lucky = 0

lucky = lucky * 33

if lucky > 0:
    lucky = lucky + 1

if storeluck > 0:
    print('Enter the store')
    if milkluck > 0:
        print('put 1 bottle of milk')
        if eggluck > 0:
            print('put 6 eggs')
            print('bro went home and told mumma he got milk and eggs')
            print('mumma : "thats my boy"')
        else:
            print('I just got milk')
    elif eggluck > 0:
        print('put 6 eggs')
        print('I just got 6 eggs')
    else:
        print('bro : "the store is open but I got nothing"')
        print('mumma : "Get your ass off"')
else:
    print('Go home')
    print('bro : "the store is closed"')
    print('mumma : "get your ass off"')

print(f"Your Luck is {lucky}%")


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
storeluck = random.randint(1,2)
milkluck = random.randint(1,2)
eggluck = random.randint(1,2)

if storeluck > 1 :
    print('Enter the store')
    if milkluck > 1 :
        print('put 1 bottle of milk')
        if eggluck > 1 :
            print('put 6 eggs')
            print('bro went home and told mumma he got milk and eggs')
            print('mumma : "thats my boy"')
        else:
            print('I just got milk')
    elif eggluck > 1 :
        print('put 6 eggs')
        print('I just got 6 eggs')
    else:
        print('bro : "the store is open but I got nothing"')
        print('mumma : "get your ass off"')
else:
    print('go home')
    print('bro : "the store is closed"')
    print('mumma : "get your ass off"')


"""
While Loop Push-up Program
"""

print('Bro : "Gotta Push-up until am tired')
pushUp = 0
totalPushUp = 0
energy = 20

while pushUp < energy + 10:
    pushUp += 1
    if totalPushUp == 10:
        print(f'u got tired and ur push up is {totalPushUp}')
    else:
        totalPushUp += 1
        print(f'current push-up : {totalPushUp}')

if totalPushUp == energy:
    print('Bro have no enemies')
else:
    print('Bro gotta hit the gym')

# With chance of tired

"""
while pushUp < energy:
    pushUp += 1
    print(f"current push-Up : {pushUp}")
    if pushUp > 15:
        print('u starting tired')
        from numpy import random
        tired = random.randint(100)
        if tired >= 10:
            print('you are tired')
            break

print(f'ur push-up is {pushUp}')
"""


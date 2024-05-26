for count, i in enumerate(range(10, 40, 5)):
    print(count, i)

fruits = ('apple', 'banana', 'orange')
print(list(enumerate(fruits, 1)))

tupl = (33, 49, 55)
myList = [10, 20, 30]
z = list(zip(tupl, myList))
print(z)

for t, m in z:
    print(t + m)

for i in range(3):
    print(tupl[i] + myList[i])

groceries = ['apples', 'chips', 'bread', 'icecream']
prices = [2, 3, 1.2, 4.25]

for food in range(4):
    print(groceries[food], '=', prices[food])

zip_shop = (zip(groceries, prices))
print(zip_shop)

for g, p in zip_shop:
    print(g, '=', p)

n1 = [100, 2, 90, 10]
n2 = [12, 7, 90, 50]

zip_n = zip(n1, n2)

for i, j in zip_n:
    if i > j:
        print(i)
    elif i < j:
        print(j)
    else:
        print(i, j)

for i in range(4):
    if n1[i] > n2[i]:
        print(n1[i])
    elif n1[i] < n2[i]:
        print(n2[i])
    else:
        print(n1[i], n2[i])

ns = list(range(10, 70, 10))
vs = [2, 5]
import  itertools
from  itertools import  cycle as cy

v1 = [2]
v2 = [5]

zipV = list(zip(ns, cy(v1), cy(v2)))
calc = []

for n, v, z in zipV:
    s = n * v
    t = n * z
    calc.append(s)
    calc.append(t)

print(calc)


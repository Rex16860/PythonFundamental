# E1
toys = {"robot": "$40.0", "car": "$25", "Ironman": "$12"}

v = list(toys.values())[0][1:]
v2 = list(toys.values())[1][1:]
v3 = list(toys.values())[2][1:]
print(int(eval(v) + eval(v2) + eval(v3)))

# E2
# question = [10, 4, 50, 90, 10, 'c', ('a', 'b', 'c'), 100, 100]
# output : true true false true false
question = [10 != 4, 50 == 50, 90 == 10, 'c' in ('a', 'b', 'c'), 100 != 100]
print(question)

# E3
films = {'k1': 'Blade runner 2049', 'k2': 'matrix', 'k3': 'terminator'}

print(len(films['k1']) > len(films['k2']) < len(films['k3']))

# E4
lifeStages = {0: 'embryo', 1: 'fetus', 2: 'baby', 3: 'infant', 4: 'teen'}
midLife = {5: 'adult', 6: 'big kid'}
lifeStages.update(midLife)

print(lifeStages)

# E5
nest1 = [(1, 2, 3), {'k1': [30, 1, 300, 2, 77], 'k2': [10, 20, 30]}, ['a', '500', 'c']]
k1 = nest1[1]['k1'][2]
k2 = nest1[1]['k2'][2]
k3 = eval(nest1[2][1])
print(k3)
print(float(nest1[0][2] + k1 + k2 + k3))

# E6
prices = ['a', 'b', '9', 'c', 'd', 'four', 'e', 'f', '2.5']
sentence = """The bill for the {}#!/,?? {}#!/ ??and drink came to {}??"""
prices = prices[2::3]

v = eval(prices[0]) + float(eval(prices[2])) + len(prices[1])
sentence = sentence.format('pizza', 'chips', '$' + str(v)).replace('??', '').replace('#!/', '')

print(v)
print(sentence)


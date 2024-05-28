import random as rd
rd.seed(10)

numbers = rd.sample(range(10, 100), k=10)
print(numbers)

print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(round(9.12345, 4))
print(abs(-200))
print(eval('20'))
print(pow(5, 3))

n_ns = sorted(numbers)

print([pow(x, 2) for x in n_ns])

print([i > 40 for i in n_ns])
print(sum([i < 40 for i in n_ns]))

data = ['10', 8.12345, 100, -30, -200]
print(data)

nData = eval(data[0]) + int(data[1]) + data[2] + abs(-30) + abs(-200)
print(nData)

cleanData = sorted([abs(k) for k in [int(i) for i in data]])[2:][::-1]
print(cleanData)
print(sorted([abs(k) for k in [int(i) for i in data]])[2:][::-1])
print('The top three values {0}, {1}, and {2}. My favourite number is {2}'. format(*cleanData))

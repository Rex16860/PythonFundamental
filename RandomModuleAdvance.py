import random as rd

# seed()
for i in range(1, 4):

    rd.seed(1)

    print(rd.randint(1, 1000))

rd.seed(3)
print(rd.randint(1, 1000))

rd.seed(3)
print(rd.randint(1, 1000))
print(rd.randint(1, 1000))

# getState()
state = rd.getstate()

print(rd.sample(range(20), k=10))

# restore state
rd.setstate(state)

print(rd.sample(range(20), k=5))

list1 = list(range(1, 7))

print(rd.choice(list1))
rd.setstate(state)
print(rd.choice(list1))

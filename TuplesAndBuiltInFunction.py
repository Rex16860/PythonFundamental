tup1 = 40, 20, 30, 10
print(tup1)

myList = list(range(10, 31, 10))
tup2 = tuple(myList)
print(type(tup2))

tup3 = tup2 + tup1
print(tup3)

tup4 = "hi", "hi", "hi", "ho", "ho", 11, 11, False
print(tup4.count("hi"))

print(sum(tup1) * 19)
print(max(tup3))

print(sorted(tup3))

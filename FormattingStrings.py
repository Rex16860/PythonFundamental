name = 'Ren'
grade = 'B'

print("The student name is {} and the grade is {}".format(name, grade))

animals = ["Tigers", "Snakes", "Eagles"]
safari = "I saw {}, {} and {}"

print(safari.format(animals[1].upper(), animals[2].capitalize(), animals[0].upper()))

print(safari.format(*animals).upper())

n = '200'
print(eval(n) + 50)

ns = [10, 20, 30, 40]
print(eval('{0} + {1} + {2} + {3}'.format(*ns)))

print("%d / %d = %.3f" % (9, 5, 9 / 5))
print('%d / %d = %.4f' % (4, 5, 4/5))

fruit = 'apple'

print('The length of this word "{}" is {}'.format(fruit, len(fruit)))

print("days left are {num: .10f}".format(num=365/12))

n = 365 / 12

print(f'the days left are {n: .10f}')

p1 = 'python'
p2 = 'Older'

print(f"""This is a docstring that is uses {p1} 3.12 and\\
can't be used for {p2} versions of {p1}""".replace('\\', '').upper())

n = [20, 50, 40]

n = n[0]
print(n)

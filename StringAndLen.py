rose = 'red'
violet = 'blue'
orange = 'orange'

print(rose, violet, orange, sep=", ")
print(rose, violet, orange, end="! ")

print("thi's 'quote' inside a string")

lower = 'hello world'
upper = 'HELLO WORLD'

print(len(lower))
print(lower.upper())
print(upper.lower())

print(type(upper))

lan = 'Python'
print('this is a cool ' + lan + " language")

n = 11
print('my favorite number is ' + str(n) + '!')

print(eval('100') - eval('50'))
print(type(eval('3.4')))

mystring = 'a a a i I i u u u'

print(mystring.count('I'))

messy = """\\Please #@clean up-- #@This messy #@Docstring 
which --Can have\\multiple lines\\
of string--"""
# print(messy)
print(messy.replace('\\', '').replace('#@', '').replace('--', ''))

fruit = "Apple"
print(fruit[0], fruit[1], fruit[1], fruit[3], fruit[len(fruit) - 1])


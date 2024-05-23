greet = "hello World"

# Slicing

print(greet[6:])

# Stride

letters = 'abcdef'
print(letters[1::2])

robot = 'technologically'

consoles = 'ps4 is cooler than xbox!'

code = 'p1y2t3h4o5n6i7c8'

words = 'I saw a cat jump over the moon into the clouds'

altWords = 'I saw a cow fly over the gates and into the forest'

paid = "I received a total of $5000"

print(len(robot))

print(robot[0:6])

print(robot[6:len(robot) - 4])

print(consoles.find('!'))

print(consoles[-5:])
print(consoles[(len(consoles) - 5):(len(consoles) - 1)])
print(consoles[-17:-11])

print(code.replace('1', '').replace('2', ''))

print(code[0:1] + code[2:3] + code[4:5])
print(code[0::2].upper())
print(code[1::2][::-2])

v = words.split()

print(v)

print(v[3:12:2])

sl = slice(3, 12, 2)

print(altWords.split())

x = altWords.split()

print(x[sl])
print(x[3:12:2])

print("cat" in v and 'cow' not in altWords)

print(" ".join(x))
print(" ".join(v))

print(paid.split('$'))
print(paid.split('$')[1])


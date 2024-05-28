# E1
def compute(rad, num):
    import random as rd

    rd.seed(10)

    numbers = range(1, rd.randint(1, rad))

    calc = []
    for i in range(len(numbers)):

        if numbers[i] % 2 == num and numbers[i] > 10:
            s = numbers[i]
            calc.append(s)
        else:
            s = 0
            calc.append(s)

    print(sum(calc))
    return calc


print(compute(20, 0))


# E2
def lang(program='PHP'):
    print('My favourite language is {}'.format(program))


def udemy(program):
    lang(program)
    print('The coolest part about {} is functions'.format(program))


udemy('Python')


def greet(name='William'):
    print('Hello there, ' + name, '!')


def repeat(n):
    for i in range(n):
        name = input('student name: ')
        greet(name)


# repeat(5)


def survivor(name='osaa'):
    zomb1 = input('How many zombies are there? ')
    zombie = eval(zomb1)

    if zombie == 0:
        print('the zombie is {}, {} is survived!'.format(name, zombie))
    elif 1 <= zombie < 20:
        print('{} is fighting {} zombies!'.format(name, zombie))
    elif 20 <= zombie < 100:
        print('{} is shooting {} zombies!'.format(name, zombie))
    elif 100 <= zombie < 200:
        print('{} is running from {} zombies!'.format(name, zombie))
    else:
        print('{} is eaten ALIVE by {} zombies!'.format(name, zombie))


survivor('ren')

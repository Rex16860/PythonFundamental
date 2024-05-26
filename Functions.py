def square(arg1=50, arg2=50):
    """This adds two numbers together"""
    return arg1 + arg2


val = square(110, 190)
print(val)


def squared(num):
    return num ** 2


def cubed(num):
    return num ** 3


def quad(num):
    return num ** 4


v = 5

print(squared(v))
print(cubed(v))
print(quad(v))

total = squared(v) + cubed(v) + quad(v)
print(total)


def greet():
    time = eval(input('Enter the time: '))

    if 6 <= time < 12:
        print('Good morning')
        return squared(time)
    elif 12 <= time < 18:
        print('Afternoon')
        return cubed(time)
    elif 18 <= time < 21:
        print('Good evening')
        return quad(time)
    else:
        print('Good morning')
        return time


n = greet()
print(type(n))

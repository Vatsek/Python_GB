def f(x):
    return x**2

g = f

print(type(f))
print(type(g))

print(f(4))
print(g(4))

def calc1(x):
    return x+10

def calc2(x):
    return x*10

def math(op, x):
    print(op(x))


math(calc2, 10)
math(calc1, 10)


def sum(x, y):
    return x+y

sum = lambda x, y: x+y # тоже самое, что и функция выше!


def mult(x, y):
    return x*y


def calc(op, a, b):
    print(op(a, b))
    # return op(a, b) если требуется вернуть а не напечатать


calc(lambda x, y: x+y, 4, 5)

List comprehension

list = []
for i in range(1, 21):
    if (i % 2 == 0):
        list.append(i)

list = [i for i in range(1, 21) if i % 2 == 0]

print(list)

def f(x):
    return x**3
list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
print(list)



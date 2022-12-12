# value = None
# print(type(value))
# a = 123
# b = 1.23
# print(a)
# print(b)
# value = 1234
# print(type(a))
# print(type(b))
# print(type(value))

# s = 'hello "world"' # можно выделить ковычками. Если нужны одинарные, то выделяем переменную двойными
# print(s) # вывод строки
# s = "hello 'world'"
# print(s) # вывод строки

# s = 'hello \'world' # использование escape последновательности
# print(s)

# s = 'hello \nworld' # переход на новую строку при помощи escape последовательности
# print(s)

# s = "hello 'world'"
# print(a,'-',b,'-',s) # вывод многих значений
# print('{} - {} - {}'.format(a, b, s)) # форматированный вывод
# print(f'{a} - {b} - {s}') # интерполяция

# print('{1} - {0} - {2}'.format(a, b, s)) # можно внутри фигурных скобок назначить где какая переменная

# f = False
# print(f)

# list = [1, 2, 3]
# print(list)

# print('Введите a: ')
# a = int(input())
# print('Введите b: ')
# b = int(input())
# print(a,b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')
# print(f'{a} + {b} = {a+b}')

# a = 1.3
# b = 3
# c = round(a * b, 3)
# print(c)

# f = [1, 2, 3, 4]
# print(f)
# print(2 in f) # получим true потому что 2 в списке есть
# print(not 2 in f) # получим false потому что 2 в списке есть

# is_odd = f[0] % 2 == 0 # проверяем есть четность нулевого элемента списка
# is_odd = not f[0] % 2 # либо так
# print(is_odd)

# a = int(input('Введите первое число'))
# b = int(input('Введите второе число'))
# if a > b:
#     print(a)
# else:
#     print(b)


# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждал Вас, Марина')
# elif username == 'Ильнар':
#     print('Ильнар - ТОП!')
# else:
#     print('Привет, ',username)

# original = 23
# inverted = 0
# while original !=0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит!')
# print(inverted)

# for i in 1, 2, 3, 4, 5:
#     print(i**2)

# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i**2)

# for i in range(5):
#     print(i)

# for i in range(1, 5):
#     print(i)

# for i in range(1, 5, 2): # третий аргумент показывает на сколько увеличивать
#     print(i)


# text = 'съешь еще этих мягких французских булок'
# print(len(text)) # 39 - показывает длину строки
# print('еще' in text) # true - показывает есть ли "еще" в тексте
# print(text.isdigit()) # false - показывает является ли строка числами
# print(text.islower()) # true - показывает все ли буквы маленькие
# print(text.replace('еще', 'ЕЩЕ')) # заменяет при выводе заданное слово на другое


# numbers = [1, 2, 3, 4, 5]
# print(numbers)

# ran = range(1, 6)
# print(type(ran))

# numbers = list(ran) # приведение типа range к типу list
# print(type(numbers))

# print(numbers)
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)
# for i in numbers:
#     i *=2
#     print(i)
# print(numbers)

# colors = ['red', 'green', 'blue']

# for e in colors: # red green blue
#     print(e)

# for e in colors: # redred greengreen blueblue
#     print(e*2)

# colors.append('gray') #  добавить в конец списка

# print(colors == ['red', 'green', 'blue', 'gray']) # true

# colors.remove('red') # delcolors[0] удалить элемент

# del colors[0]

def f(x):
    if x == 1:
        return 'целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2.3
print(f(arg))
print(type(f(arg)))
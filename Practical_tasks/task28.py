# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций
#  допускаются только +1 и -1. Также нельзя использовать циклы.

a = int(input('Введите число A: '))
b = int(input('Введите число B: '))


def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a+1, b-1)

print(f'Сумма чисел {a} и {b} равна: {sum(a, b)}')

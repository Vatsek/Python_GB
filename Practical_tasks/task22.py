# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого набора. 
# m - кол-во элементов второго набора. 
# Значения генерируются случайным образом.
# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
# 6 12

import random
n = int(input('Введите количество элементов первого набора: '))
m = int(input('Введите количество элементов второго набора: '))

def fill_list(lenght):
    numbers = []
    for i in range(0, lenght):
        random_number = round(random.randint(0, 10))
        numbers.append(random_number)
    return numbers

set_numbers1 = fill_list(n)
set_numbers2 = fill_list(m)


print(f'Первый набор элементов: {set_numbers1}')
print(f'Второй набор элементов: {set_numbers2}')

result = []

for i in set_numbers1:
    if i in set_numbers2:
        result.append(i)

result = set(result)
if len(result) == 0:
    print('В наборах нет повторяющихся чисел')
else:
    print(f'Повторяющиеся числа в обоих наборах в порядке возрастания: {sorted(result)}')
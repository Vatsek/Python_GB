# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

while True:
    try:
        n = int(input('Введите до какого числа включительно вывести все степени двойки: '))
        result = 1
        i = 0
        print(f'Все целые степени двойки до {n}:')
        while result <= n:
            print(result, end = ' ')
            result *= 2
        break
    except:
        print('Некорректный ввод. Попробуйте еще раз')

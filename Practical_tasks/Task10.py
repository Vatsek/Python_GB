# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были
#  повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random
while True:
    try:
        count = int(input('Введите количество монеток: '))
        coins = []
        tails = 0
        eagles = 0

        for el in range(0, count):

            side = round(random.randint(0, 1))

            coins.append(side)

            if side == 0:
                tails += 1

            else:
                eagles += 1

        print(coins)

        if tails < eagles:
            print(f'Требуется перевернуть {tails} монетки(ку)(ок) с решкой сверху, что бы все монетки были'
                  ' \n повернуты вверх одной стороной')
            break
        elif eagles < tails:
            print(f'Требуется перевернуть {eagles} монетки(ку)(ок) с орлом сверху, что бы все монетки были'
                ' \n повернуты вверх одной стороной')
            break
            
        else:
            print('Не имеет значения какие монетки переворачивать')
            break
    except:
        print('Некорректный ввод. Попробуйте еще раз')

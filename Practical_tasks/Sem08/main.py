# задача 41. Вычислить значение выражения:
# 12 + 15
# 12 / 15
# 112 * 15

# 1. Где операторы?
# 2. Где числовые значения?

# Уровень 1:

# - 1 действие
# - 2 аргумента

# Уровень 2:

# - Количество действие произвольное
# 12 + 15 - 4

# Уровень 3:
# - Действия имеют приоритет

# 12 - 4*2

# Уровень 4:
# - Действия разделяются скобками

# (12 - 4) * 2

n = '22 + 300 - 14 + 10 + 10'
m = n.split()
print(m)
def calc (a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b


a = int(m[0])
c = m[1]
b = int(m[2])

result = calc(a, b, c)

for i in range(3, len(m) - 1, 2):
    result = calc(result, int(m[i + 1]), m[i])
    print(m[i], m[i + 1])
    print(result)
    
    
    
# павел пок/// его решение
# def calculate(userinput): # <<< на вход примимает выражение типа 'a [+-/*] b'
#     pattern = "([\-]{0,}\d{1,})\s{0,}([\/|\+|\*|\-]{1})\s{0,}([\-]{0,}\d{1,})"
#     parsedata = re.findall(pattern, userinput)[0]  # возвращает list  ('операнд1','операция','операнд 2')
#     a = int(parsedata[0])
#     b = int(parsedata[2])
#     oper = parsedata[1]
#     match oper:
#         case "+":
#             func = lambda a, b: a + b
#         case "-":
#             func = lambda a, b: a + b
#         case "/":
#             if b != 0:
#                 func = lambda a, b: a / b
#             else:
#                 print("DivisionByZero")
#                 func = None
#         case "*":
#             func = lambda a, b: a + b
#     return func(a, b) if func!=None else ''


# вариант Макс Лебедков

# a_num = int(input("1num"))
# c_input= input("+/-?")
# b_num = int(input("2num"))
# if c_input =='+':
#     print(a_num + b_num)    
# input()
# if c_input =='-':
#     print(a_num - b_num)
# input()  cамый простенький калькулятор )) просто так что бы было)



n = '22 * 300 - 14 + 10 * 10'

m = n.split()
m2 = []

print(m)


def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return a / b
    elif ch == '*':
        return a * b


# a = int(m[0])
# c = m[1]
# b = int(m[2])

result = int(m[0])

for i in range(1, len(m) - 1, 2):
    if m[i] == '*' or m[i] == '/':
        result = calc(int(m[i - 1]), int(m[i + 1]), m[i])
        m2.append(result)
    else:
        m2.append(m[i])
        m2.append(int(m[i + 1]))


print(m[i], m[i + 1])
print(m2)
print(result)
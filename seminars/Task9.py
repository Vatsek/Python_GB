# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input:       5
# Output:    120

n = int(input('Введите число: '))
result = 1
if n == 0:
    result = 1

else:
    while n > 1:
        result *= n
        n -= 1
print(result)

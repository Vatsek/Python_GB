
#ваня
n = int(input())
max_number = 1000
while n != 0:
   n = int(input())
   if max_number > n:
       max_number = n
print(max_number)


#петя
n = int(input())
max_number = -1
while n < 0:
   n = int(input())
   if max_number < n:
       n = max_number
print(n)


правильное решение: 
n = int(input('введи число N:'))
if n!=0:
    max_number = n
    while n != 0:
        if max_number < n:
            max_number = n
        n = int(input('введи следуещее число N:'))
    print('максимальное число {}'.format(max_number))
else:
    print('чисел нет')
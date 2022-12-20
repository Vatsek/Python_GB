# задача 23
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
#  больших предыдущего (элемента с предыдущим номером) 


# Input: [0, -1, 5, 2, 3]
# Output: 2 

# пояснение
# (-1 < 5, 2 < 3)

import os
os.system('clear')

это для MacOS

array = [0, -1, 5 ,2 ,3, 3, 9, 7, 6, 9]
count = 0
for i in range(0, len(array)-1):
    if array[i] < array[i+1]:
        count += 1
        
        print(array)
        print(count)
        
        print('\n\n\n')
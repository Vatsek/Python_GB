# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое
# значение некоторой характеристики, и возвращают True, если это так. Если значение характеристики для 
# разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

# values = [0, 2, 10, 6]

# def same_by(f, list_num):
#     # return set(map(f, list_num))
#     return True if len(set(map(f, list_num))) == 1 else False

# print(values)
# print(same_by(lambda x: x % 7, values))
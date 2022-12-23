# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2



# string = "a a a b c a a d c d d".split(" ")
# line =""
# for el in string:
#     line += el

# def count_of_word(line):
#     mas = []
#     result = []
#     for el in line:
#         if el in mas:
#             result.append(el+ "_" + str(mas.count(el) +1))
#         else:
#             result.append(el)
#         mas.append(el)
#         restult_str = ""
#     for el in result:
#         restult_str += el + " "

#     return restult_str

# print(count_of_word(line))
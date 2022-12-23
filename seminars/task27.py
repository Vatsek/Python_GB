# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. 
# So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13


# 2 задача
# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных 
# целых чисел. Требуется определить значение наибольшего элемента последовательности, которая завершается 
# первым встретившимся нулем (число 0 не входит в последовательность)”. Однако 2  друга оказались не такими 
# смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок 
# в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.

st = "She sells sea shells on the sea shore;\
The shells that she sells are sea shells I'm sure.\
So if she sells sea shells on the sea shore,\
I'm sure that the shells are sea shore shells."
print(st)
st = st.lower()
st = st.replace(',', " ")
st = st.replace('.', " ")
st = st.replace(';', " ")
st = st.replace('\'', " ")
words = set(st.split())
print(words)
print(len(words))



степик
codewars
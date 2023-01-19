# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt
# Структура данных:
# Фамилия, имя, отчество, номер телефона.
# Пример данных:
# Ivanov, Ivan, Ivanovich, +79111234567
# Petrov, Petr, Petrovich, +79119876543
# Функции справочника:
# - Показать все записи
# - Найти запись по вхождению частей имени
# - Найти запись по телефону
# - Добавить новый контакт
# - Удалить контакт
# - Изменить номер телефона у контакта
# Пример работы программы:
# При запуске программы пользователю выдается меню: 

# Введите номер действия:
# 1 - Показать все записи +
# 2 - Найти запись по вхождению частей имени +
# 3 - Найти запись по телефону +
# 4 - Добавить новый контакт +
# 5 - Удалить контакт
# 6 - Изменить номер телефона у контакта
# 7 - Выход

# .
# После выбора действия выполняется функция, реализующая это действие. 
# После завершения работы функции пользователь возвращается в меню.




import os

def clear_screen():
    os.system('clear')

phonebook = 'phonebook.txt'
    
def print_all_data(file_name):
    with open(file_name, 'r') as data:
        print('Все записи в записной книжке:\n')
        for line in data:
            print(line)
        print()

def find_by_name(file_name, search_value):
    values = []
    with open(file_name, 'r+') as data:
        for line in data:
            values.append(line.split())
    count = 0
    for i in values:
        if search_value in i:
            print(values[count])
        count += 1

def find_by_phone(file_name, search_value):
    values = []
    with open(file_name, 'r+') as data:
        for line in data:
            values.append(line.split())
    count = 0
    for i in values:
        
        if search_value in i[3]:
            print(i)
        count += 1


def add_new_contact(file_name):
    with open(file_name, 'a') as data:
        data.write(input('Введите фамилию: ') + ' ')
        data.write(input('Введите имя: ') + ' ')
        data.write(input('Введите отчество: ') + ' ')
        data.write(input('Введите номер телефона: ') + '\n')
        print('Успешно добавлено')

menu = 'Возможные действия программы: \n\n 1 - Показать все записи \n 2 - Найти запись по вхождению частей имени\n \
3 - Найти запись по телефону\n 4 - Добавить новый контакт \n 5 - Удалить контакт \n 6 - Изменить номер телефона у контакта \n 7 - Выход'


while(True):

    print(menu + '\n')
    command = input('Введите номер действия: ')
    print()

    match command:
        case '1':
            print_all_data(phonebook)
            print()
        case '2':
            find_by_name(phonebook, input('Введите что то из ФИО поиска: '))
            print()
        case '3':
                find_by_phone(phonebook, input('Введите телефон для поиска: '))
                print()
        case '4':
            add_new_contact(phonebook)
            print()
        case '7':
            clear_screen()
            break
        case _:
            print("Действия с данным номером не найдно" + '\n')


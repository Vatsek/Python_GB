import file_name as file

def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result

def save_data_to_file(name, data_list):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(data_list +'\n')
        
def print_data(file_name):
    with open(file_name, 'r', encoding='utf8') as data:
        for line in data:
            print(line)
    print()

def add_bus():
    save_data_to_file(file.buses, input("Введите параметры автобуса: "))
    print('\nУспешно добавлено\n')

def add_driver():
    save_data_to_file(file.drivers, input("Введите водителя: "))
    print('\nУспешно добавлено\n')

def add_route():
    save_data_to_file(file.routes, input("Введите маршрут: "))
    print('\nУспешно добавлено\n')

def find_by_value(): # найти по значению
    files = [file.buses, file.drivers, file.routes]
    search_value = input('Введите что ищем: ')
    print()
    for i in files:
        values = read_data_from_file(i)
        availability = False    
        for i in values:
            if search_value in i:
                availability = True
                for j in i:
                    print(j, end=' ')
                print()
    print()
    if availability == False: print('Данные не найдены\n')
    
def print_routes_details():
    yes_or_no = input('Хотите отобразить детали маршрута (y/n)?: ')
    if yes_or_no == 'n':
        return
    search_value = input('Введите номер маршрута для отображения детализации: ')
    print()
    route = read_data_from_file(file.routes)
    routes_details = []
    availability = False
    for i in route:
        if search_value in i:
            availability = True
            route = i
    if availability == False:
            print('Такого маршрута не найдено\n')
            return
    routes_details.append(f'Номер маршрута: {route[1]}')
    bus = read_data_from_file(file.buses)
    for i in bus:
        if route[2] in i:
            routes_details.append(f'Гос номер автобуса: {i[1]}')
    driver = read_data_from_file(file.drivers)
    for i in driver:
        if route[3] in i:
            routes_details.append(f'Фамилия водителя: {i[1]}')
    for i in routes_details:
        print(i)
    print()
    
def del_value(file_name, message): # удалить
    del_value = input(message)
    print()
    values = read_data_from_file(file_name)
    availability = False
    with open(file_name, 'w',encoding='utf8') as data:
        for i in values:
            if del_value in i:
                availability = True
                print('Успешно удален\n')
                continue
            for j in i:
                data.write(str(j))
                if j != i[-1]:
                    data.write(',')
            data.write('\n')
    if availability == False: print('Нет данных для удаления\n')
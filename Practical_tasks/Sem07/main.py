import function as fn
import file_name as file

menu = [
        ("1", "Вывод автобусов"),
        ("2", "Добавление автобуса"),
        ("3", "Удаление автобуса"),
        ("4", "Вывод водителей"),
        ("5", "Добавление водителей"),
        ("6", "Удаление водителей"),
        ("7", "Вывод маршрутов, детализация маршрута"),
        ("8", "Добавление маршрута"),
        ("9", "Удаление маршрута"),
        ("10", "Поиск по значению"),
        ("11", "Выход")]


while(True):
    
    for i in menu:
        print(f'{i[0]} - {i[1]}')
        
    command = input('Введите номер действия: ')
    print()
    
    match command:
        case '1':
            fn.print_data(file.buses)
        case '2':
            fn.add_bus()
        case '3':
            fn.del_value(file.buses, 'Введите гос номер или id автобуса, который хотите удалить: ')
        case '4':
            fn.print_data(file.drivers)
        case '5':
            fn.add_driver()
        case '6':
            fn.del_value(file.drivers, 'Введите фамилию или id водителя, которого хотите удалить: ')
        case '7':
            fn.print_data(file.routes)
            fn.print_routes_details()
        case '8':
            fn.add_route()
        case '9':
            fn.del_value(file.routes, 'Введите id маршрута, id автобуса, id водителя или номер маршрута который хотите удалить: ')
        case '10':
            fn.find_by_value()
        case '11':
            exit()
        case _:
            print("Действия с данным номером не найдно" + '\n')
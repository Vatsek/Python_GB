# test = 'test.txt'
# numbers = []
# with open(test, 'r') as phone:
#     for line in phone:
#         numbers.append(line.split())

# print(numbers)

# temp = numbers[0]

# print(temp)

# temp.pop(2)
# temp.insert(2, 64)
# print(temp)

# print(numbers)

# with open(test, 'w') as phone:
#     for i in numbers:
#         for j in i:
#             phone.write(str(j))
phone = 'test.txt'
del_contact = 'Вацек'

# ________________________________
def list_from_text(file_name):
    values = []
    with open(file_name, 'r+') as data:
        for line in data:
            line = line.replace(',', ' ')
            values.append(line.split())
    return values

print(list_from_text(phone))

def del_contact(file_name, del_value):
    del_value = del_value.lower()
    print(del_value)
    values = list_from_text(file_name)
    with open(file_name, 'w') as data:
        for i in values:
            # print(type(i)) тут нужно что то придумать, как сравнить в нижнем регистре!
            if del_value in i:
                continue
            for j in i:
                data.write(str(j)+' ')
            data.write('\n')
                
                
del_contact(phone, 'Павел')
    
def print_all_data(file_name):
    with open(file_name, 'r') as data:
        print('Все записи в записной книжке:\n')
        for line in data:
            print(line)
        print()

print_all_data(phone)           
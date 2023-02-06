import datetime

file_name = 'date.txt'

def read_data_from_file(file_name) -> list[str]:
    with open(file_name, 'r', encoding='utf8') as datafile:
        result = datafile.read().split('\n')
        lib: dict = {}
        for item in result:
            date_tmp = item[0].split('.')
            lib[item[1]] = datetime(date_tmp[2], )
        
read_data_from_file(file_name)


datetime.strptime(date, "%Y/%m/%d")


# datew.year
# datew.month
# datew.day
# datew.hour

# student_tuples = [
#         ('john', 'A', 15),
#         ('jane', 'B', 12),
#         ('dave', 'B', 10),
# ]
# sorted(student_tuples, key=lambda student: student[2])   # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

from datetime import datetime

birthdays = []

todays = datetime.now()
year = todays.year
with open("date.txt", "r", encoding="utf8") as file:
    for line in file:
        days = line.strip("\n").split(" ")
        dd, mm, _ = days[0].split(".")
        birthdays_str = "{}.{}.{}".format(dd, mm, year)
        birthdays_data = datetime.strptime(birthdays_str, "%d.%m.%Y")
        # print(birthdays)
        name = days[1]
        birthdays_real = datetime.strptime(days[0], "%d.%m.%Y")
        # print(birthdays_real)
        age = int((birthdays_data-birthdays_real).days/365.25)
        birthdays.append((birthdays_real, name,(birthdays_data - todays).days,age))
        
       


birthdays_sort = sorted(birthdays,key=lambda x: x[2])
print(todays)
print(birthdays_sort)
for item in birthdays_sort:
    if item[2]>0:
        print('{} исполняется {} годик, через {} день'.format(item[1],item[3],item[2]))
    elif item[2]==0:
        print('{} исполняется {} годик, СЕГОДНЯ!!!'.format(item[1],item[3],item[2]))
        
        
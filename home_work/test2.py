# list to store file lines
lines = []
test = 'test.txt'
# read file
with open(test, 'r') as phonebook:
    # read an store all lines into list
    for line in phonebook:
        lines.append(line.split())


print(lines)


with open(test, 'w') as fp:
    # iterate each line
    for number, line in enumerate(lines):
        # delete line 5 and 8. or pass any Nth line you want to remove
        # note list index starts from 0
        if number not in [4, 7]:
            fp.write(line)







# print_all_data('test.txt')

# result = readFile('test.txt')
# print(result)
# print(type(result))

# if '123' in result[0]:
#     print(result[0])


# line_num = 0
# search_phrase = "the dog barked"
# for line in f.readlines():
#     line_num += 1
#     if line.find(search_phrase) >= 0:
#         print line_num
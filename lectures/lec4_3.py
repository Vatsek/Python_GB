li = [x for x in range(1,20)]

li = list(map(lambda x: x+10, li))

print(li)

data = [x for x in range(10)]

# result = list(filter(lambda x: x%2==0, data))
result = list(filter(lambda x: not x%2, data)) # not %2 тоже самое что и x%2 == 0

print(result)

# ZIP

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14 ,7]
salary = [111, 222, 333]

data = list(zip(users, ids, salary))
print(data)

users = ['user1', 'user2', 'user3', 'user4', 'user5']
data = list(enumerate(users))
print(data)

user_info = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(user_info)
user_info['email'] = 'new_email'
print(user_info)

print(user_info.get('name'))

if user_info.get('age'):
    print(f"{user_info.get('age')} old")
else:
    print("You are young")

user_info.update({'Country': 'USA'})
print(user_info)

user_info.update({'age': 31})
print(user_info)

user_info.pop('name')
print(user_info)

keys = user_info.keys()
print(keys)

for key in user_info.keys():
    print(key)

values = user_info.values()
print(values)

for values in user_info.values():
    print(values)

items = user_info.items()
print(items)

for key, value in user_info.items():
    print(f"{key}: {value}")

print(f"{user_info.get('state')}")

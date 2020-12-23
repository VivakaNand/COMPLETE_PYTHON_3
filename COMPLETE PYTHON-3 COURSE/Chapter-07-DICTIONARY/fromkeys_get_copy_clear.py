# fromkeys
d = {'name': 'unknown', 'age': 'unknown'}


# d = dict.fromkeys(['name', 'age', 'height'], 'unknown')
# d = dict.fromkeys(('name', 'age', 'height'), 'unknown')
# d = dict.fromkeys(range(1,11), 'unknown')
# d = dict.fromkeys('abc', 'unknown')  # 'a': , 'b':, 'c':
# d = dict.fromkeys(['name', 'age'], ['unknown','unknown'])
# d = dict.fromkeys(['name', 'age'], 'unknown')
# print(d)

# get method (usefull)
d = {'name': 'Vivek', 'age': 'unknown'}
# print(d['name']) # returns vivek
# print(d['names']) # returns error, to handle this error use get method
#print(d.get('name')) # returns vivek
# print(d.get('names')) # returns None


# if 'name' in d:
#     print('present')
# else:
#     print('Not present')


# if d.get('name'):
#     print('present')
# else:
#     print('Not present')

# if None ---> False, else ----> True

#d.clear()
#print(d)

d1 = d.copy()
#d1 = d
#print(d1.popitem())
#print(d)
#print(d1)

print(d1 is d)  # False
print(d1 == d)  # True
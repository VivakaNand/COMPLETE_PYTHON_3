# summary dictionary
# what is dictionary
# unordered collection of data

d = {'name':'Vivek', 'age':25}

# or 

d1 = dict(name = 'Vivek', age = 25)

# or

d2 = {
    'name' : 'Vivek',
    'age' : 25,
    "fav_mov" : []
}


# how to access data from dictionaries
# NOTE- There is no inxeding because of unordered collections
#print(user1['name'])
#print(user1['age']) 


# which type of data a dictionary can store ?
# anything
# number, string, list, dictionary

user_info = {
    'name' : 'Vivek',
    'age' : 25,
    'fav_mov': ['Ex Mcahina', 'her', 'I robot'],
    'fav_game': ['circket', 'football'],
}

# print(user_info['fav_mov'])


# How to add data to empty dictionary
user_info2 = {}
user_info2['name'] = 'Vivek'
user_info2['age'] = 25
print(user_info2)


# add and delete data
# # how to add data
user_info['fav_songs'] = ['song1', 'song2']
# print(user_info)


# # pop method
# popped_item = user_info.pop('fav_game')
# print(type(popped_item))
# print(user_info)


# popitem method
popped_item = user_info.popitem()
print(user_info)
print(type(popped_item))

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

# more about get, two same keys in dictionaries
user = {'name': 'Vivek', 'age': 34, 'age': 54} # if two same keys then next key overwrites
#print(user.get("name", "Not found !")) # if key is not present we can get a message 
print(user)


#d.clear()
#print(d)

d1 = d.copy()
#d1 = d
#print(d1.popitem())
#print(d)
#print(d1)

print(d1 is d)  # False
print(d1 == d)  # True


# in keyword and iterations in dictionary


# # check if key exist in dictionary
# if 'name' in user_info:
#     print('Present')
# else:
#     print("Not present")


# # check if value exist in dictionary ---> values method
# if 25 in user_info.values():
#     print("Present")
# else:
#     print("Not Present")

# # loops in dictionaries
# for i in user_info.values():
#     print(i)


# # values method
# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))

# # keys method 
# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))


# # loop in dictionaries
# for i in user_info:
#     print(user_info[i])


# # items methos
# user_items = user_info.items()
# print(user_items)
# print(type(user_items))
# [('name', 'Vivek'), ('age', 25), ('fav_mov', ['Ex Mcahina', 'her', 'I robot']), ('fav_game', ['circket', 'football'])]


for keys, values in user_info.items():
    print(f"key is {keys} and values is {values}")


#more_info  = {'state': 'Sindh', 'Country': 'Pakistan'}
more_info  = {'name' : 'vivek','state': 'Sindh', 'Country': 'Pakistan'}  # no change


# user_info.update(more_info)
user_info.update({})

print(user_info)


# word counter

def word_counter(s):
    dic = {}
    for i in s:
        dic[i] = s.count(i)
    return dic

print(word_counter('vivek'))
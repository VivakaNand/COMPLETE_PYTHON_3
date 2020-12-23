# in keyword and iterations in dictionary

user_info = {
    'name' : 'Vivek',
    'age' : 25,
    'fav_mov': ['Ex Mcahina', 'her', 'I robot'],
    'fav_game': ['circket', 'football'],
}

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
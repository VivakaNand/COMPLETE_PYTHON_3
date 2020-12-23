# add and delete data
user_info = {
    'name' : 'Vivek',
    'age' : 25,
    'fav_mov': ['Ex Mcahina', 'her', 'I robot'],
    'fav_game': ['circket', 'football'],
}

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
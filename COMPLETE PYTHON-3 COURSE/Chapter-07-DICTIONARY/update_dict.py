user_info = {
    'name' : 'Vivek',
    'age' : 25,
    'fav_mov': ['Ex Mcahina', 'her', 'I robot'],
    'fav_game': ['circket', 'football'],
}

#more_info  = {'state': 'Sindh', 'Country': 'Pakistan'}
more_info  = {'name' : 'vivek','state': 'Sindh', 'Country': 'Pakistan'}  # no change


# user_info.update(more_info)
user_info.update({})

print(user_info)
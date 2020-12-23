# user_info = {
#     'name' : 'Vivek',
#     'age' : 25,
#     'fav_mov': ['Ex Mcahina', 'her', 'I robot'],
#     'fav_game': ['circket', 'football'],
# }

name = input("Enter your name : ")
age = input("Enter your age : ").split(',')
fav_mov = input("Enter your favourite movies separated by comma : ").split(',')
fav_songs = input("Enter your favourite songs separated by comma : ").split(',')

user = {}

user['name'] = name
user['age'] = age
user['fav_mov'] = fav_mov
user['fav_songs'] = fav_songs

for key, value in user.items():
    print(f'{key} : {value}')
    
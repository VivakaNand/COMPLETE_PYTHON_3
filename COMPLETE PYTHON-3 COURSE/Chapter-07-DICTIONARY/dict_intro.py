# dictionaries intro
# Q - why we use dictionaries?
# A - Because of limitations of lists, lists are not enough 
# to represent real data

# example
user = ['vivek', 25, ['Ex Mcahina', 'her', 'I robot'], ['circket', 'football']]
# this list contains user name , age , fav movies , fav games
# you can do this but this is not good way to do this.


# Q - What are dictionaries
# A - unordered collections of data in key :value pair.


# how to create dictionaries
user = {'name': 'vivek', 'age': 24}
# print(user)
# print(type(user))


# second method to create dictionaries
user1 = dict(name = 'Vivek', age = 25)
#print(user1)


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
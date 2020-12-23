# zip function

user_id = ['1','2','3']
names = ['Vivek', 'Madan', 'Aneel']
last_name = ['Jetani', 'jatin', 'jetani']
# output - ('1','Vivek'), ('2','Madan'), ('3','Aneel')
# print(list(zip(user_id, names)))
print(list(zip(user_id, names, last_name)))
#print(dict(zip(user_id, names, last_name))) # error dict required 2 items

# convert tuple list to dictionary
example = [('1', 'Vivek'), ('2', 'Madan'), ('3', 'Aneel')]
# print(dict(example))
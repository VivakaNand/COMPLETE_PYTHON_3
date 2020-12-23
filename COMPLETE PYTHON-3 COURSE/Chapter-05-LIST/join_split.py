# split method is used to split sting into list
# convert string to list
# user_info = "Vivek 24".split() # it splits string to list and seperate by space
# print(user_info)

# user_info = "Vivek,24".split(",") # it splits string to list and seperate by comma
# print(user_info)

# name, age = "Vivek,24".split(",") # it splits string to list  into two variables and seperate by comma
# print(name)
# print(age)

# name, age = input("Enter your name and age : ").split(",") # it splits string to list  into two variables and seperate by comma
# print(name)
# print(age)


#Join method
# convert list to string
user_info = ['Vivek', '24']
print(','.join(user_info))

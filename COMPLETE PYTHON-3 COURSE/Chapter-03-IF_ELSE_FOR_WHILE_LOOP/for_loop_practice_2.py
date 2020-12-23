# practice for loop 
# ask user name and count each character
# "Vivwk Jetani"

# output :
# V : 1
# i : 2
# v : 1
# e : 2
# k : 1
#   : 1
# J : 1
# t : 1
# a : 1
# n : 1

name = input("Enter your name : ")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        count = name.count(name[i])
        print(f"{name[i]} : {count}")
        temp += name[i]

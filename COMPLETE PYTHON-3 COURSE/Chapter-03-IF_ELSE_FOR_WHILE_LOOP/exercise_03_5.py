# ask a user for name 
# Example - Vivek Jetani
# print count of words
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

name = input("Enter your Full name : ")
temp_var = ""
i = 0
while i<len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i += 1
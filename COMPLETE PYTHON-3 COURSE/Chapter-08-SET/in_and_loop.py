# in keyword in sets and for loop
# we use set to remove duplicates and also to perform set operations

s = {'a', 'b', 'c'}

# # in keyword to check if item is present or not in set
# if 'a' in s:
#     print("present")
# else:
#     print("not present")


# # for loop
# for item in s:
#     print(item)

s1 = {1,2,3,4}
s2 = {3,4,5,6}

# union operation "|" pipe
union_set = s1 | s2
print(union_set)

# union operation "&" pipe
print(s1 & s2)

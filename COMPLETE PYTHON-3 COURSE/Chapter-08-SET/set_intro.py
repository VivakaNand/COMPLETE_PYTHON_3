# set data type
# unordered(not index wise) collection of unique items

# s = {1,2,3}
# print(s) # only unique values 
# print(s[1])  # error

# 1. can store int, float, string in set
# 2. can't store list and dict inside set
# 3. if two values 1 and 1.0 or 3 and 3.0 considers both same

s = {1,1.0,2.3,'string'}
# print(s)
# output - {1, 2.3,'string'}

# s = {1,1.0,2.3,'string', {1},[1]} # error


# # remove duplicates in list
# l = [1,2,3,2,2,3,4,7,7,5,6,4,6]
# print(l)
# s2 = set(l) # unique values in set
# print(s2)
# l2 = list(set(l))
# print(l2) # unique list

# # add values in set
# s.add(4) # add 4 in s
# s.add(5) # add 5 in s
# s.add(4) # no change in set 
# print(s)

# remove in set
#s.remove(3) # if 3 is in set it removes otherwise rise error
# s.discard(3) # if 3 is in set it removes otherwise does not rise error
# print(s)

# # clear set
# s.clear()
# print(s)

# # copy set
# s2 = s.copy()
# print(s2)


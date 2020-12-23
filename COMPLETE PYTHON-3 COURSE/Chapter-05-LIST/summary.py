# list chapter summary
# list is a data structure that can hold any type of data

# create list
words = ["word1", "word2"]

# you can store anything inside list
mixed = [1,2,3, [4,5,6], 'seven', 8.0,None]

# list is ordered collection of items
# print(mixed[0]) # output = 1
# print(mixed[3]) # output = [4,5,6]

# add data to our list
# append method

# mixed.append("10")
# mixed.append([10,20,30])  # it adds as it list at the end as one element
# print(mixed)

# extend method
# mixed.extend([10,20,30]) # it adds all elements of list at the end
# print(mixed)

# join method
# join two list
# l = l1 + l2

# insert method
# mixed.insert(1, 'inserted') # it adds elements in the specefic position
# print(mixed)

# remove data from list
# # pop method
# poped = mixed.pop() # removes last item
# popped = mixed.pop(1) # remove item at 1 position
# print(poped)
# print(popped)

#remove method
# mixed.remove('seven')
# print(mixed)

# del statement
# del mixed[3]
# print(mixed)

# loop in list
for i in mixed:
    print(i)
# some more methods to add data in our list
# append method
# insert method
# how to join(concatenate) two list
# extend method
# difference b/w append and extend method



# append method    # it adds in the last position of list
fruits = ['mango', 'orange']
fruits.append('apple')   
print(fruits)

# insert method # it add elenent at any position in list by using index
fruits1 = ['mango', 'orange']
fruits1.insert(1, 'apple')  # it insert 'mango' at 1 position  
print(fruits1)

# how to join(concatenate) two list
fruits2 = ['grape', 'apple']
fruit = fruits1 + fruits2    # add elements at the end of list
print(fruit)

# extend method
fruits1.extend(fruits2) # it append fruits2 elements in fruits1
print(fruits1)

# append method
fruits1.append(fruits2) # it append list in list
print(fruits1)

# difference b/w append and extend method
# extend - appends elements of list into list
# append - appends list in the list
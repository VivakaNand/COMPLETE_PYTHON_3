# iterator vs iterables

numbers = [1,2,3,4] # List, tuple, string --- iterables
squares = map(lambda a:a**2, numbers) # iterators

# for i in squares:
#     print(i)

# number_iter = iter(numbers) # creating iterable to iterator
# print(next(number_iter)) # 1
# print(next(number_iter)) # 2
# print(next(number_iter)) # 3
# print(next(number_iter)) # 4
# print(next(number_iter))  # StopIteration error


# print(next(numbers)) # iterable object

# square is iterator
print(next(squares))
print(next(squares))
print(next(squares)) 
print(next(squares))

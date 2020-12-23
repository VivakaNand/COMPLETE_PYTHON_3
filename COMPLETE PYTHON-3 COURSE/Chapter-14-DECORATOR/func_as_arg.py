# map
# def square(a):
#     return a**2
l = [1,2,3,4,5]
# print(list(map(square, l)))

#print(list(map(lambda a:a**2, l)))

# def my_map(func, l):
#     new_list = []
#     for item in l:
#         new_list.append(func(item))
#     return new_list
# print(my_map(lambda a:a**3, l))

# list comprehension
def my_map(func, l):
    return [func(item) for item in l]
print(my_map(lambda a:a**3, l))

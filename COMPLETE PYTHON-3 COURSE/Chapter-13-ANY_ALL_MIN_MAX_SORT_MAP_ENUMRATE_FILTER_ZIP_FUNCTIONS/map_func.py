# map function

numbers = [1,2,3,4]
#output - [1,4,9,16]

def square(a):
    return a**2

# map function  
squares = list(map(square, numbers))
print(squares)

# map function with lambda
squares = list(map(lambda i:i**2, numbers))
print(squares)

# list comprehension
squares_new = [i**2 for i in numbers]
print(squares_new)

# simple for loop
new_list = []
for i in numbers:
    new_list.append(square(i))
print(new_list)

# length of string
name = ['abc', 'abcdef', 'dsfsesef']
length = map(len, name)
for i in length:
    print(i)

length = list(map(len, name))
print(length)
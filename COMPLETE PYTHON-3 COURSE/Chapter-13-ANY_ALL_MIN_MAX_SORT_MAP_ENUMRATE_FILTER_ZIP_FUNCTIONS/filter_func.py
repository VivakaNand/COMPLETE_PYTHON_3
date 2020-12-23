# filter function

# Even function
def is_even(a):
    return a%2==0

num = [1,2,4,5,6,7,7,8,5,4,6,7,8,10]
even = filter(is_even, num)
# one time iterable
for i in even:
    print(i)
print(even)

# tuple
even1 = tuple(filter(is_even, num))
print(even1)

# List
even2 = list(filter(is_even, num))
print(even2)

# lambda
even3 = filter(lambda a:a%2==0, num)
print(list(even3))

# list comprehension
even4 = [i for i in num if i%2==0]
print(even4)

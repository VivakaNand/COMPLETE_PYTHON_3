# any , all function

number1 = [1,3,4,7,9]
number2 = [1,2,3,4,5,6]

# all function
print(all([num%2==0 for num in number1])) # True -- if all number in list are even else False

# any function
print(any([num%2==0 for num in number1])) # True -- if any number in list is even else False



# for loop
even1 = []
for num in number1:
    even1.append(num%2==0)
# print(even1)

# list comprehension
# even2 = [num%2==0 for num in number1]
# print(even2)

# print(all([True,True,True,True,True])) #---True
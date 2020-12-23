# list comprehension
# with the help of list comprehension we can create a list in one line

# # create a list of squares from 1 to 10
# squares = []
# for i in range(1, 11):
#     squares.append(i**2)
# print(squares)

# squares2 = [i**2 for i in range(1, 11)]
# print(squares2)


# negative = []
# for i in range(1, 11):
#     negative.append(-i)
# print(negative)

# negative2 = [-i for i in range(1, 11)]
# print(negative2)

names = ['Vivek', 'Madan', 'Aneel']
new_name = []
for name in names:
    new_name.append(name[0])
print(new_name)

new_name2 = [name[0] for name in names]
print(new_name2)
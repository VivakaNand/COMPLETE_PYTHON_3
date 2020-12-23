# Advance min() max() function

# number = [1,2,3,4,5,7]
# print(min(number))

# # dedine function
# def func(item):
#     return len(item)
# names = ['Vivek', 'xyzesd', 'abc']
# print(min(names, key = func))

# # lambda function
# names = ['Vivek', 'xyzesd', 'abc', 'bc']
# print(min(names, key = lambda item: len(item)))


students1 = {
    'Vivek' : {'score':90, 'age':25},
    'Madan' : {'score':70, 'age':24},
    'Aneel' : {'score':75, 'age':23}
}
print(min(students1, key = lambda item:students1[item]['age']))


# students2 = [{'name':'Vivek','score':90, 'age':25},
#             {'name':'Madan','score':70, 'age':24},
#             {'name':'Aneel','score':75, 'age':23}]
        
# print(min(students2, key = lambda item:item.get('age'))['name'])

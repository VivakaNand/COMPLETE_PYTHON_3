# list comperehension in nasted list

 # example = [[1,2,3], [1,2,3], [1,2,3]]
nested_comp = [[i for i in range(1,4)] for i in range(3)]
print(nested_comp)

new_list = []
for i in range(3):
    new = []
    new_list.append(new)
    for i in range(1,4):
        new.append(i)
print(new_list)
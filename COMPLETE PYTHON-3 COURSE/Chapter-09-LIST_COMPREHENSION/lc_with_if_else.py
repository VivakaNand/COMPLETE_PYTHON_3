# list comperehension with if else
num = [1,2,3,4,5,6,7,8,9,10]

# output - [-1,4,-3,16,-5,36,-7,64,-9,100]

new_list = []
for i in num:
    if i%2 == 0:
        new_list.append(i**2)
    else:
        new_list.append(-i)
print(new_list)


# list comperehension method
def new_list(l):
    return [i**2 if i%2==0 else -i for i in l]
print(new_list(num))
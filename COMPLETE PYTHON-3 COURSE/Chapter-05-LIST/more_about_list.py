# generate lists with range functions
# somthing more about pop method
# index method
# pass list to a function

#number  = list(range(1,11))
number = [1,2,3,1,4,5,6,7,1,7,9]
#print(number)
#popped_item = number.pop()
#print(popped_item)

#print(number.index(1, 4, 10))  # index (item, start position, stop position)

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(number))
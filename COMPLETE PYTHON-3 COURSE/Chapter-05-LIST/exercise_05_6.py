# last exercise
# function 
# [1,2,3 [1,2], [3,4]], input
# 2
# type()

lst = [1,2,3, [1,2],[1,2], [3,4]]

def count_list(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count
        
print(count_list(lst))
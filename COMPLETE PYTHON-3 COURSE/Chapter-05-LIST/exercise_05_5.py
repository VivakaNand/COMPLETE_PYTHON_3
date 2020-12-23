# example 
# input ---> [1,2,3,4,5] , [1,2,6,7,8]
# output ---> [1,2]
lst1 = [1,2,3,4,5]
lst2 = [1,2,6,7,8]

def same_finder(l1, l2):
    out = []
    for i in l1:
        if i in l2:
            out.append(i)
    return out
print(same_finder(lst1, lst2))

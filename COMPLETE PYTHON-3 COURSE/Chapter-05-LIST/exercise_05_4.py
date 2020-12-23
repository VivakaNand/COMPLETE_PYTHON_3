# filter odd even

# define a function
# input
# list ---> [1,2,3,4,5,6,7,8]

# output ----> [[1,3,5,7], [2,4,6,8]]
num = [1,2,3,4,5,6,7,8]
def even_odd_filt(l):
    even = []
    odd = []
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    output = [even, odd]
    return output
print(even_odd_filt(num))
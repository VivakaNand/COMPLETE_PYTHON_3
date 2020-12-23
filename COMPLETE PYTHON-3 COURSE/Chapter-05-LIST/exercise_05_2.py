# define a function which will take list as a argument and this function
# will return a reversed list

# solution
# def reverse_list(l):
#     l.reverse()
#     return l

def reverse_list(l):
    return l[::-1]

def rev_by_pop(l):
    reverse = []
    for i in range(len(l)):
        i = l.pop()
        reverse.append(i)
        
    return reverse

number = list(range(1,11))
print(reverse_list(number))
print(rev_by_pop(number))
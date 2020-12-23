# define a function that take list of words as arguments and return 
# list with reverse of every element in that list

# example
# ['abc', 'def', 'xyz'] ---> ['cba', 'fed', 'zyx']
lst = ['abc', 'def', 'xyz']
def rev_list(l):
    reverse = []
    for i in l:
        reverse.append(i[::-1])
    return reverse
print(rev_list(lst))
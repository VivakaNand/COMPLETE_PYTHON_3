# define a function that take list of strings
# list containing reverse of every string 

# NOTE - USE LIST COMPREHENSION

# example
l = ['abc', 'edf', 'xyz']
# reverse_string(l) -----> ['cba', 'fde','zyx']

def reverse_string(l):
    return [i[::-1] for i in l]
print(reverse_string(l))


def reverse_str(l):
    new_list = []
    for i in l:
        new_list.append(i[::-1])
    return new_list
print(reverse_str(l))
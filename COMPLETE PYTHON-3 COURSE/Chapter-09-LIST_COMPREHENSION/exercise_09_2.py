# num to string
# define a function

# example
# input = [True, False, [1,2,3], 1,1.0,3]
# output ----> ['1','1.0','3']

l = [True, False, [1,2,3], 1,1.0,3]

def list_str(l):
    return [str(i) for i in l if (type(i) == int or type(i) == float)]
print(list_str(l))

def bool_ty(l):
    return [str(i) for i in l if (type(i) == bool)]
print(bool_ty(l))
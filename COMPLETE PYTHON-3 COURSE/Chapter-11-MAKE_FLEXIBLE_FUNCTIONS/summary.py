# only two argument
def add(a,b):
    return a+b
#print(add(2,3))

# many arguments
def new_add(*args):
    # 1,2,3,4
    # (1,2,3,4), # ([1,2,3,4])
    total = 0
    for num in args:
        total += num
    return total

#print(new_add(1,2,3,4,5))

#l = (1,2,3,4) # also can pass tuples
l = [1,2,3,4]
#print(new_add(*l))


# kwargs - keyword arguments , **
def func(**kwargs):
    print(kwargs) # gather as dictionary
    print(type(kwargs))

#func(name = ' Vivek', age = 24, gwnder = 'M')


# kwargs, args, norma;, default
# PADK- parameter, args, default , kwargs

def func2(name, *args, age = 25, **kwargs):
    print(name)
    print(args)
    print(age)
    print(kwargs)

func2("Vivek", *l,24, a = 4, b=1)


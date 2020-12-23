# *args with normal parameter

def multiply_num(num,*args):
    total = 1
    print(num)
    print(args)
    for i in args:
        total *= i
    return total
print(multiply_num(2,2,3,4,5)) # first parameter is num and other are *args

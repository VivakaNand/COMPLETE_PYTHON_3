# functions with all parameters
# very important to understand

# PADK - 
# prameter
# *args
# default parameters
# **kwargs

def func(name, *args, age = 25, **kwargs):
    print(name)
    print(args)
    print(age)
    print(kwargs)
func('Vivek', 1,2,3, a=1,b=2)

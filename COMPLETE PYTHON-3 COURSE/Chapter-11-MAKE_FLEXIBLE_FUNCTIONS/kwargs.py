# kwargs (keyword arguments)
# **kwargs {double star operator}

# kwargs as a parameter
def func(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k} : {v}")

#func(name = 'Vivek', age = 25)

# dictionary unpacking
d = {'name' : "Vivek", 'age': 25}
func(**d)
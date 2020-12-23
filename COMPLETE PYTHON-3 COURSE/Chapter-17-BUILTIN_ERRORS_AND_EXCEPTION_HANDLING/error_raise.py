def add(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError("OOPs you have passed wrong inputs")

print(add('1',2))
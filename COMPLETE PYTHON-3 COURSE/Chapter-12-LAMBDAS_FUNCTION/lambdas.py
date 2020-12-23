# lambdas expressions (anonymous function)

def add(a,b):
    return a+b
print(add(2,3))


add2 = lambda a,b : a+b
print(add2(4,5))

multiply = lambda a,b : a*b
print(multiply(3,4))

print(add)
print(add2)
print(multiply)
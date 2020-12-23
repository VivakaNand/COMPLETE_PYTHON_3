
def greater(a,b):
    if a>b:
        return a
    return b

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c

def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger, c)

print(new_greatest(100,60,30))

# kiss - keep it simple stupid

# function inside function
# greater(a, b) --> a or b
# greater(a or b, c) -------> greatest

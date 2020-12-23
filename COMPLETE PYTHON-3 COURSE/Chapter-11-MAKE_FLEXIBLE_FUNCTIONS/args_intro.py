# make flexible functions

# *operator
# *args

def total(*args):
    total = 0
    for i in args:
        total += i
    return total

print(total(1,2,3,4,5,6))
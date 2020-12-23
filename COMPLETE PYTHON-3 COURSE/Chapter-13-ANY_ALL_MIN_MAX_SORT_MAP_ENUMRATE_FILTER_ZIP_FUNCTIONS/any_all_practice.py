# any all function

def my_sum(*args):
    # args = ()
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total =0
        for i in args:
            total += i
        return total
    else:
        return "Wrong input"
print(my_sum(1,2,3,4,5,6,7,8))

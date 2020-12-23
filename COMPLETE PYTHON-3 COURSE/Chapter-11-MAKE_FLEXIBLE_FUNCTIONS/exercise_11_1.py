#num = int(input('Enter a number : '))

def cube_num(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "You didn't pass any args"

nums = [1,2,3]
print(cube_num(3, *nums))
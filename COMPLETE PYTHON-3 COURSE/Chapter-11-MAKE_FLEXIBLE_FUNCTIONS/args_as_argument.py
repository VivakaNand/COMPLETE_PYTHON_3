def multiply_num(*args):
    total = 1
    print(args) # ([2,3,4])
    for i in args:
        total *= i
    return total

# if we pass list or tuple as argument we have to apply '*' with argument
# otherwise it prints whole list or tuple as one element
num = [2,3,4] 
# num = (2,3,4)
# print(multiply_num(num)) #[2, 3, 4]
print(multiply_num(*num)) #[2, 3, 4]
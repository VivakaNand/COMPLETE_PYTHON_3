# scope
x = 5 # global variable

def func():
    global x # to use global variable inside function
    x = 7  # local variable
    return x
print(x)      # global 5
print(func()) # global inside function 7
print(x)      # 7
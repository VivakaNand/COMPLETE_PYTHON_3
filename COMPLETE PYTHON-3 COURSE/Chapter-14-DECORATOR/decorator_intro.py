# Decorators - enhance the functionality of other functions
# @ use for decorator

def decorator_function(any_function):
    def wrapper_function():
        print("This is awesome function")
        any_function()
    return wrapper_function


# This is awesome function
@decorator_function # shortcut
def func1():
    print('This is function 1')

func1()

# This is awesome function
@decorator_function
def func2():
    print('This is function 2')

func2()

# we can also use func name as variable
# func2 = decorator_function(func2)
# func2()
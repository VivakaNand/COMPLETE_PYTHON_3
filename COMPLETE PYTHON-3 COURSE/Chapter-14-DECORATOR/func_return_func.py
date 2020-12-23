# function returning function

def outer_func():
    def inner_func():
        print("Inside inner function")
    return inner_func
var = outer_func()
var()

def outer_func2(msg):
    def inner_func2():
        print(f"Message is {msg}")
    return inner_func2
msg = outer_func2('Hello ther !')
msg()
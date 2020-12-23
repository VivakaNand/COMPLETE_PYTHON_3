from functools import wraps
def only_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(arg) == data_type for arg in args]):
                return function(*args, **kwargs)
            return "Invalid arguments"
        return wrapper
    return decorator

# @only_data_type_allow(str)
# def string_join(*args):
#     string = ""
#     for i in args:
#         string += i
#     return string

# print(string_join('Vivek', 'Vishan', 'Jetani'))

@only_data_type_allow(int)
def square(*args):
    square = []
    for i in args:
        square.append(i**2)
    return square
print(square(1,2,3,4,5,6,7,8,9,10))
# make a function "divide"\
# divide(a,b)
# exception handling 

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err: # print default error
        #print("You can\'t divide anumber by zero")
        print(err)
    except TypeError as err:
        print('number must be int or floats')
    except:
        print('unexpected error')

print(divide('2',f0))
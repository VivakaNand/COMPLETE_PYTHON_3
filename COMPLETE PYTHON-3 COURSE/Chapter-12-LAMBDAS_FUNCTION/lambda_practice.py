# lambda expression practice
# Even odd functions in three methods
# Method-1
def is_even(a):
    if a%2 ==0:
        return True
    else:
        return False

# print(is_even(5)) # False
# print(is_even(4)) # True

# Method-2
def is_even(a):
    return a%2 ==0

#print(is_even(5)) # False
#print(is_even(4)) # True

# Method-3 Lambda
is_even = lambda a : a%2==0
#print(is_even(5)) # False
#print(is_even(4)) # True


# last character
def last_char(s):
    return s[-1]
#print(last_char('Vivek'))

last_char = lambda s : s[-1]
#print(last_char('Vivek'))

# lambda with if , else
def func(s):
    if len(s) > 5:
        return True
    return False
#print(func('asasfgd'))

def func(s):
    return len(s) > 5
#print(func('asasfgd'))

# with lambda 
func = lambda s : True if len(s) > 5 else False
#print(func('asd'))

# more simple
func = lambda s : len(s)>5
print(func('abcdgf'))
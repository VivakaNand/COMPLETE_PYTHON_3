# Exercise 
# define a function that takes a number(n)
# return a dictionary containing cube of numbers from 1 to n

# example
# cube_finder(3)
# {1:1, 2:8, 3:27}

num = int(input("Enter a number : "))
def cube_finder(l):
    dic = {}
    for i in range(1,l+1):
        dic[i] = i**3
    return dic
print(cube_finder(num))


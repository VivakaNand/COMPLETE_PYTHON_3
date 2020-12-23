# define a function which will take a list containing numbers as 
#input and return list containing square of every elements.

# example
# number = [1,2,3,4,5]
#square_list(numbers) ------> return ----> [1,4,9,16,25]

number = [1,2,3,4,5]
def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square
print(square_list(number))
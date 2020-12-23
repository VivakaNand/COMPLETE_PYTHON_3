# THIS IS CHALLENGE

# define a function take any no of lists containing any number
# [1,2,3] , [4,5,6], [7,8,9]
# return average
# (1+4+7)/3, (2+5+8)/3, (3+6+9)/3


# def average_finder(l1, l2, l3):
#     average = []
#     for pair in zip(l1,l2, l3):
#         average.append(sum(pair)/len(pair))
#     return average
# print(average_finder([1,2,3] , [4,5,6], [7,8,9]))


# def average_finder(*args):
#     average = []
#     for pair in zip(*args): # * to unzip tuples
#         average.append(sum(pair)/len(pair))
#     return average
#print(average_finder([1,2,3] , [4,5,6], [7,8,9]))


# try to make this anonymous function in one line using Lambda 

average_finder = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
print(average_finder([1,2,3] , [4,5,6], [7,8,9], [10,11,12]))
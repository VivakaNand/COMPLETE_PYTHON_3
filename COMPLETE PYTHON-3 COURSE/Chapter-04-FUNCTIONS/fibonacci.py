# fibonacci series
# 0 1 1 2 3 5 8 134 21 34

# 1 ---> 0
# 2 ---> 0 1
# 3 ---> 0 1 1

# for i in range(0, 11):
#     print(i, end = " ")

def fibonacci_seq(n):
    a = 0 # first number
    b = 1 # second number
    if n == 1:
        print(a)
    elif n == 2:
        print(a, b)
    else:
        print(a,b, end = " ")
        for i in range(n-2):
            c = a + b  # c = 1 , 2 , 3
            a = b      # a = 1 , 1 , 2
            b = c      # b = 1 , 2 , 3
            print(b, end = " ")

fibonacci_seq(10)

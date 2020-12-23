# define generator function
# take one number as argument
# generate a sequence of even numbers from 1 to that number

def even_num(n):
    for i in range(2,n+1,2):
        yield(i)

    # for i in range(1,n+1):
    #     if i%2==0:
    #         yield(i)
#even = even_num(20)
# for num in even:
#     print(num)

# if we assign variable to our generator it generates one sequence on every for loop
# but when we apply direct for loop on generator it generates sequence every time Like
for num in even_num(20):
    print(num)

for num in even_num(20):
    print(num)
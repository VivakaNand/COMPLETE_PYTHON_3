# Create your first generator with generator function
# 1.) generator function

# 10, 1 to 10

def nums(n):
    for i in range(1, n+1):
        yield(i)          # yeild - to generate generators

number = nums(10)
# print(number)

for num in number:
    print(num)

for num in number:
    print(num)


# memory (list)
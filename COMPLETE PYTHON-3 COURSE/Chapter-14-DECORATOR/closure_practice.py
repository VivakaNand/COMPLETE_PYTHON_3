# function returning (closure) practice

# cube
# square
# power

def to_power(n):
    def calc_power(x):
        return x**n
    return calc_power

# Cube
cube = to_power(3)
print(cube(2))

square = to_power(2)
print(square(4))
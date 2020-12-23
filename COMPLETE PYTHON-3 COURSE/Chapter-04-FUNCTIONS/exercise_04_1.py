# function which returns greater number
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

def greater_num(a,b):
    if a>b:
        return f"The greater number is {a}"
    return f"The greater number is {b}"
print(greater_num(num1,num2))
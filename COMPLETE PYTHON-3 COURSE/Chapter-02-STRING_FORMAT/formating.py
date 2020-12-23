name = "Vivek"
age = 24

print("Hello " +name + " your age is " + str(age))  # ugly syntax
# string formating
# python 2
# python3
# python 3.6

# python3
print("Hello {} your age is {} ".format(name, age))
print("Hello {} your age is {} ".format(name, age+2))

#Python 3.6
print(f"Hello {name} your age is {age} ")
print(f"Hello {name} your age is {age + 2} ")
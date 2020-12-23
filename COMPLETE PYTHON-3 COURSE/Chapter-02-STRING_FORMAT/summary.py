# strings
name = "Vivek"

# String Indexing
print(name[-1])

# String Slicing
print(name[-1:0:-1])

# take user input
age = int(input("Enter your age : ")) # string
print(age)

#take two user inputs
user_name, age = input("Enter your name and age : ").split(",")
print(user_name)
print(age)

# len function
print(len(name))

# lower, upper, title method
r_pos = name.find("v")
r_pos_2 = name.find("v", r_pos +1)
print(r_pos_2)

#center method  **Vivek**
print(name.center(9, "*"))

# string are immutable
# name[2] = "s"
print(name.replace("h", "H", 1))
print(name)
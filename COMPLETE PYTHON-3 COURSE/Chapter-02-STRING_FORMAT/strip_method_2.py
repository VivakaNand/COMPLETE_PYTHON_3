# replace() method

string = "She is beautiful and she is good dancer"
print(string.replace(" ", "_"))
print(string.replace("is", "was"))
print(string.replace("is", "was", 1))

# find() method
print(string.find("is"))
print(string.find("is", 1))
print(string.find("is", 5))

# Center() method
name = "Vivek"
# # **Vivek**, 5 + 4
print(name.center(9, "*"))
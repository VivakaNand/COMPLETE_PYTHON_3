name, char = input("Enter comma seperated name and character : ").split(",")
print(f"length of your name is {len(name)}")
print(f"character count : {name.strip().lower().count(char.strip().lower())}") # case sensitive

# remove space 
# " Vivek " -----> "Vivek" --------> "vivek"
# "  V " -------> "H" --------> "h"
#name.strip().lower().count(char.strip().lower())
#char.strip().lower()
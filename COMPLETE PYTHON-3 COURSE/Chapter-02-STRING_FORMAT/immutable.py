# string are immutable
string = 'string'
print(string[1])
#string[1] = "T" # can't directly change string
print(string.replace("t", "T"))
print(string)
new_string = string.replace('t', 'T')
print(new_string)
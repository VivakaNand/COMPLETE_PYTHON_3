name = "    Vivek    "
dots = ".............."

# lstrip() method # remove blank space from left side
print(name+dots)
print(name.lstrip() + dots)

# rstrip() method # remove blank space from right side
print(name+dots)
print(name.rstrip() + dots)

# strip() method # remove blank space from both side
print(name+dots)
print(name.strip() + dots)

# replace method remove space from every where
name1 = "   Vi  v   ek   "
print(name1+dots)
print(name.replace(" ", "") + dots)
# list vs strings

# strings are immutable
# lists are mutable

# immutable (can't change)
s = "string"
s.title()  # no change in string
print(s)  
t = s.title()
print(t) # change in string when store in new variable


# mutable (can change)
l = ["word1",  ' word2', 'word3']
l.append("word3")
print(l)
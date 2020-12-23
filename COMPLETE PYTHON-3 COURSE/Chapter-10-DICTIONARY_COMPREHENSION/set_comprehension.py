# sets comprehension 
s = {i**2 for i in range(1,11)}
print(s)

# names first letter set
names = ['Vivek','Aneel', 'Madan']
new = {i[0] for i in names}
print(new)
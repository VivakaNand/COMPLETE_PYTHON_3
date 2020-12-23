# read file 
# open file
# read method
# seek method # toset the cursor position
# tell method # to point out cursor position
# readline method # read line by line
# readlines method
# close method

f = open('file.txt')
#print(f'cursor position - {f.tell()}')
#print(f.read())
#print(f'cursor position - {f.tell()}')
#print('before seek method')
#f.seek(0)
#print('after seek method')
#print(f'cursor position - {f.tell()}')
#print(f.read())
#f.close()

# readline # read line by line
#print(f.readline(), end ='')
#print(f.readline(), end ='')
#print(f.readline(), end ='')

# readlines # read all line in a list
#lines = f.readlines()
#print(line)
#for line in lines:
#    print(line)


# name ,closed
print(f.name)
print(f.closed)
f.close()
print(f.closed)

f = open(r"C:\new\vivek\file.txt")
# \t , \n
# window - \
# linux ,mac- /
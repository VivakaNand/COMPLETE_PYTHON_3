#f = open('file.txt')
#f.read()
#f.close()

with open('file.txt') as f:
    data = f.read()
    print(data)
print(f.closed)
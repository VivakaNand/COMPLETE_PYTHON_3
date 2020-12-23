# break and continue keyword

# 1 to 10 print
# break statement 
print("Break Satatement")
print("Range number 1 to 10, but break before 5")
for i in range(1, 11):
    if i == 5:
        break
    print(i) # it print 1,2,3,4

# continue statement
# print 1 to 10, but not 5
# 1,2,3,4,6,7,8,9,10

print("Continue Satatement")
print("Show number 1 to 10, but not 5")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

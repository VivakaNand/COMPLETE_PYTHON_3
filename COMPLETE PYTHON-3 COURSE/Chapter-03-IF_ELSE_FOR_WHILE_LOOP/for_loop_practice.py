# practice for loop
# ask user a number like 123456
# calculate sum of digits ---> 1+2+3+4+5+6

# logic 
# num = "12345", length = 4
# int(num[0]) ---> 1
# int(num[1]) ---> 2
# int(num[2]) ---> 3
# int(num[3]) ---> 4
# int(num[4]) ---> 5
# i = 1 to 4

num = input("Enter a number : ")
total = 0
for i in range(0, len(num)):
    total += int(num[i])
print(total)
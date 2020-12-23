# EXERCISE - WATCH COCO
# Ask user's name and age
# if user's name start with  ('a' or 'A') and age is above 10 then
# print 'you can watch coco movie'
# Else print 'sorry, you can't watch coco'

name = input("Enter your name : ")
age = int(input("Enter your age : "))

if (name[0] == "a" or name[0] == "A") and age >= 10:
    print("You can watch coco movie")
else:
    print("Sorry, you can't watch coco")

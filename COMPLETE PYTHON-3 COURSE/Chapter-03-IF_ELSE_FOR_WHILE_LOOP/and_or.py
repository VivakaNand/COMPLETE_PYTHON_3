# check two condition at same time
# and, or
name = input("Enter your name : ")
age = int(input("Enter your age : "))

# and condition
if name=='Vivek' and age==25: # both condition must be true
    print("Condition is True")
else:
    print("Condition False")


# or condition
name1 = 'Sanjay'
age1 = 21
if name=='Sanjay' or age==25: # one condition must be true
    print("Condition is True")
else:
    print("Condition False")

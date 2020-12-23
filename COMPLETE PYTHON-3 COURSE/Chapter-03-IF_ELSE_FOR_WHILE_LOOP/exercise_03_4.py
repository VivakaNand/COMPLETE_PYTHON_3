# Problem
# ask user to input a number containing more than one digit
# exampe - 12345
# calculate 1 + 2 + 3 + 4 + 5 and print

n = input("Enter number contains more than one digit: ")
total = 0 
i = 0
length = len(n) - 1

while i<=length:
    total += int(n[i])
    print(f"Digit at {i} position is {int(n[i])}")
    i += 1
print(total)
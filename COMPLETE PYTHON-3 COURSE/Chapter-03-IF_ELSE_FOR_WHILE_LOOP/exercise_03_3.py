# Exercise one of three
# sum of n natural numbers
# ask a user for natural number (n)
# print total from 1 to n

num = int(input("Enter a Natural Number : "))

total = 0
i = 1
while i<=num:
    total += i
    print(f"Natural Numner {i} and Total {total}")
    i += 1
print(total)
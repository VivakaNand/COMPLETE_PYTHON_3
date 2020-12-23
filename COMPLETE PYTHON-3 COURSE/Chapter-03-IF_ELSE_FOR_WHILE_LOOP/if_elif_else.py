# 1 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

age = int(input("Enter your age : "))

if age == 0 or age < 0:
    print("You can not watch.!")
elif 0<age<=3:
    print("Ticket Price : Free")
elif 3<age<=10:
    print("Ticket Price : 150")
elif 10<age<=60:
    print("Ticket Price : 250")
else:
    print("Ticket Price : 200")
        
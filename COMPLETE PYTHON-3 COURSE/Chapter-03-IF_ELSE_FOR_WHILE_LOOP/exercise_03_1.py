# EXERCISE, NUMBER GUESSING GAME
# Make a variable, like winning_number and assign number to it.
# Ask user to guess a number.
# if user guassed correctly then print "You win !!!!"
# if user didn't guessed correctly then :
    # if user guessed lower than actual number then print "too low"
    # # if user guessed higher than actual number then print "too high"  

win_num = 70
user_num = int(input("Guess a Number between 1 to 100 : "))
if user_num == win_num:
    print("YOU WIN !!!!")
else:
    if user_num < win_num:
        print("Too low")
    else:
        print("Too high")
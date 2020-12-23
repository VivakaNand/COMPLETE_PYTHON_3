# default parameters


def user_info(first_name, last_name = "unknown", age = 25): # we can assign default parameters after positional parameters
    print(f"Your first name is {first_name}")
    print(f"Your last name is {last_name}")
    print(f"Your age is {age}")

user_info('Vivek', 'Jatin', 24)

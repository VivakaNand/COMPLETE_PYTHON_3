# Define is_palingrome function that take one word in string as a input
# and return True if it is palindrome else return False

# palindrome - word that reads same backwords as forwards

# example 
# is_palindrome("madam") ----> True
# is_palindrome("naman") ----> True
# is_palindrome("receive") ----> False

word = input("Input your name : ")
# def is_palindrome(word):
#     reversed_word = word[::-1]
#     if reversed_word == word:
#         return True
#     else:
#         return False

# print(is_palindrome(word))


# def is_palindrome(word):
#     if word == word[::-1]:
#         return True
#     return False

# print(is_palindrome(word))



def is_palindrome(word):
    return word == word[::-1]
    
print(is_palindrome(word))
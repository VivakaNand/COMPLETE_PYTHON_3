# dictionary comprehension
# output = square  = {1:1,2:4,3:9}

# square = {f"Square of {num} is":num**2 for num in range(1, 11)}
# for k, v in square.items():
#     print(f"{k} : {v}")


string = 'VivekVishan'
# for i in string:
#     print(i)

# {'V':2, 'i':2}
word_count = {num:string.count(num) for num in string}
print(word_count)
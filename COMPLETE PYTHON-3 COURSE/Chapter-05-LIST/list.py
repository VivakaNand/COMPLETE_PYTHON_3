# data structure
# list ---> this chapter
# ordered collection of times

# you can store any thing in list int, float, string

numbers = [1, 2, 3, 4]
print(numbers[1])

words = ["word1", "word2", "word3"]
print(words[:2])

mixed = [1, 2, 3, 4, 'five', 'six', 2.3, None]
print(mixed[-1])

mixed[1] = ['two', 'three']
print(mixed)

mixed[1:] = ['two', 'three', 'four', 5, 6, 0]
print(mixed)

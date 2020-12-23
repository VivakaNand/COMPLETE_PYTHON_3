# word counter

def word_counter(s):
    dic = {}
    for i in s:
        dic[i] = s.count(i)
    return dic

print(word_counter('vivek'))
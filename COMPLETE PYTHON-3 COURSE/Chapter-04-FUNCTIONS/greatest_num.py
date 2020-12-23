def greatest_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c
print(greatest_num(50,60,30))
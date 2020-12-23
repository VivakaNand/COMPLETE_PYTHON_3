# Exception handling
# try except else finally

while True:
    try:
        age = int(input('Enter yur age: ')) # seven # 7
        break
    except ValueError:
        print('maybe you entered string insteat of number, try again')
    except:
        print('unexpected error...')

if age < 18:
    print('You can\'t play game.')
else:
    print('You can play this game.')
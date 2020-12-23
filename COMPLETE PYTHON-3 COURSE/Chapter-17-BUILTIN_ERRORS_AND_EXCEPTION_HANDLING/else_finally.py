# else and finally clause in exception handling

while True:
    try:
        number = int(input('Enter a number : '))

    except ValueError:
        print('Please type integer !!')
    except:
        print('unexpected error !!!')
    else:
        print(f'user input = {number}')
        break
    finally:
        print('finally blocks .......') 
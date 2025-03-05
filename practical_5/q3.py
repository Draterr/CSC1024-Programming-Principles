i = 1
while i <= 60:
    if i % 2 == 0:
        if i % 12 != 0:
            print('0',end='')
        else:
            print()
    else:
        print('1',end='')
    i+=1

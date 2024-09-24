for i in range(10):
    print('i = ', i)
    if i == 0:
        i=+1
    if i == 1:
        i=+2
    if i == 2:
        continue
    if i == 3 or i == 4:
        print('Переменная равна 3 или 4')
    elif i in [5,6,7]:
        print('Переменная равна 5,6 или 7')
    else:
        break

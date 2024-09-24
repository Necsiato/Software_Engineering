num = (input('Введите число от 0 до 10: '))
if num.isdigit() and int(num)<10 and int(num)>0:
    if 0<int(num)<=3:
        print('Число от 0 до 3')
    elif int(num) <=6:
        print('Число от 3 до 6')
    else:
        print('Число от 6 до 10')
else:
    print('Неверный ввод')
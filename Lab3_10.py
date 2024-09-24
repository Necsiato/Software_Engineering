array = [2,4,5,8,10]
flag = False
for value in array:
    if value % 2 ==1:
        flag=True

if flag is True:
    print('В массиве есть нечетное число')
else:
    print('В массиве все числа четные')
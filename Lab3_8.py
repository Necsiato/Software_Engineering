value = 0
while value < 100:
    if value == 0:
        value +=5
    if value % 5 == 0 or value > 10:
        value *=6
    else:
        value // 5
    print(value)
import random

def cube():
    value = random.randint(1,6)
    print(f'Значение кубика = {value}')

    if value >= 5:
        print('Вы победили')
    elif value > 2 and value < 5:
        cube()
    else:
        print("Вы проиграли")

if __name__ == '__main__':
    cube()
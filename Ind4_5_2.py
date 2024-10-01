from Ind4_5_1 import geronfun

def main():
    print('Введите длины сторон')
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))

    print(f"Площадь = {geronfun(a,b,c)}")

if __name__ == '__main__':
    main()
# Тема 4. Функции и модули.
Отчем по теме #4 выполнил(а):
- Клейн Денис Романович
- АИС-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | - |
| Задание 7 | + | - |
| Задание 8 | + | - |
| Задание 9 | + | - |
| Задание 10 | + | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Напишите функцию, которая выполняет любые арифметические действия и выводит результат в консоль. Вызовите функцию используя “точку входа”.

```python 
def main():
    print(9*9)

if __name__ == '__main__':
    main()
```

### Результат.
![1 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_4/pic/4.1.png)

## Лабораторная работа №2
### Напишите функцию, которая выполняет любые арифметические действия, возвращает при помощи return значение в место, откуда вызывали функцию. Выведите результат в консоль. Вызовите функцию используя “точку входа”.

```python
def main():
    return 2+2

if __name__ == '__main__':
    print(main())
```
### Результат.
![2 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_4/pic/4.2.png)

## Лабораторная работа №3
### Напишите функцию, в которую передаются два аргумента, над ними производится арифметическое действие, результат возвращается туда, откуда эту функцию вызывали. Выведите результат в консоль. Вызовите функцию в любом небольшом цикле. На скриншоте ниже приведен пример программы, в которой аргумент функции “x“ превращается в параметр “one”, то же самое происходит с “y” и “two”.

```python
def main(one, two):
    result = one + two
    return result

for i in range (5):
    x = 1
    y = 10
    answer = main(x,y)
    print(answer)
```
### Результат.
![3 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_4/pic/4.3.png)

## Лабораторная работа №4
### Напишите функцию, на вход которой подается какое-то изначальное неизвестное количество аргументов, над которыми будет производится арифметические действия. Для выполнения задания необходимо использовать кортеж “*args”.

```python
def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))
    print(f"one={one} \n two={two}\n three={three}")

    return x + sum(args) / float(len(args))

if __name__ == '__main__':
    result = main(1,2,3,4,5,6,7,8,9,10)
    print(f"\nresult= {result}")
```
### Результат.
![4 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_4/pic/4.4.png)

## Лабораторная работа №5
### Напишите функцию, которая на вход получает кортеж “**kwargs” и при помощи цикла выводит значения, поступившие в функцию. На скриншоте ниже указаны два варианта вызова функции с “**kwargs” и два варианта работы с данными, поступившими в эту функцию. Комментарии в коде и теоретическая часть помогут вам разобраться в этом нелегком аспекте. Вызовите функцию используя “точку входа”.

```python
def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])

    print()

    for key in kwargs:
        print(f"{key} = {kwargs[key]}")

if __name__ == '__main__':
    main(x=[1,2,3], y=[3,3,0], z = [2,3,0], q = [3,3,0], w=[3,3,0])
    print()
    main(**{'x' : [1,2,3], 'y' : [3,3,0]})
```
### Результат.
![5 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_4/pic/4.5.png)

## Лабораторная работа №6
### Напишите две функции. Первая – получает в виде параметра “**kwargs”. Вторая считает среднее арифметическое из значений первой функции. Вызовите первую функцию используя “точку входа” и минимум 4 аргумента.

```python
def main(**kwargs):
    for i,j in kwargs.items():
        print(f"{i}. Mean = {mean(j)}")

def mean(data):
    return sum(data) / float(len(data))

if __name__ == '__main__':
    main(x=[1,2,3], y=[1,2,3])
```
### Результат.
![6 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_4/pic/4.6.png)

## Лабораторная работа №7
### Создайте дополнительный файл .py. Напишите в нем любую функцию, которая будет что угодно выводить в консоль, но не вызывайте ее в нем. Откройте файл main.py, импортируйте в него функцию из нового файла и при помощи “точки входа” вызовите эту функцию.

```python
def say_hello():
    print('Hello!')
```
```python
from Lab4_7 import say_hello

if __name__ == '__main__':
    say_hello()
```
### Результат.
![7 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_4/pic/4.7_1.png)
![7 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_4/pic/4.7_2.png)

## Лабораторная работа №8
### Напишите программу, которая будет выводить корень, синус, косинус полученного от пользователя числа.

```python
import math

def main():
    value = int(input('Введите значение: '))
    print(math.sqrt(value))
    print(math.sin(value))
    print(math.cos(value))

if __name__ == '__main__':
    main()
```
### Результат.
![8 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_4/pic/4.8.png)

## Лабораторная работа №9
### Напишите программу, которая будет рассчитывать какой день недели будет через n-нное количество дней, которые укажет пользователь. В результате день недели указан в виде цифры, где 1 = понедельник, 2 = вторник, 3 = среда и так далее.

```python
from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(
        f"Сегодня {dt.today().date()}. "
        f"День недели - {dt.today().isoweekday()}"
    )
    n = int(input('Введите кол-во дней: '))
    today = dt.today()
    result = today+td(days=n)
    print(
        f"Через {n} дней будет {result.date()}. "
        f"День недели - {result.isoweekday()}"
    )

if __name__ == '__main__':
    main()
```
### Результат.
![9 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_4/pic/4.9.png)

## Лабораторная работа №10
### Напишите программу с использованием глобальных переменных, которая будет считать площадь треугольника или прямоугольника в зависимости от того, что выберет пользователь. Получение всей необходимой информации реализовать через input(), а подсчет площадей выполнить при помощи функций. Результатом программы будет число, равное площади, необходимой фигуры.

```python
global result

def rectangle():
    a = float(input('Ширина = '))
    b = float(input('Высота = '))
    global result
    result = a*b

def triangle():
    a = float(input('Основание = '))
    h = float(input('Высота = '))
    global result
    result = 0.5 * a * h

figure = input('1 - прямоугольник, 2 - треугольник: ')

if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

print(f"Площадь = {result}")
```
### Результат.
![10 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_4/pic/4.10.png)

## Самостоятельная работа №1
### Дайте подробный комментарий для кода, написанного ниже. Комментарий нужен для каждой строчки кода, нужно описать что она делает. Не забудьте, что функции комментируются по-особенному.

```python
# Импортируем класс datetime из библиотеки datetime.
from datetime import datetime
# Импортируем функцию sqrt из библиотеки math.
from math import sqrt

# Определяем функцию main, которая принимает произвольное количество именованных аргументов.
def main(**kwargs):
    """
    Вычисляет длину по теореме Пифагора
    Параметры:
        **kwargs (словарь) - Значения начала и конца
    Возвращает:
        float: длина
    """
    # Проходимся по элементам kwargs с ключом key
    for key in kwargs.items():
        # Вычисляем длины вектора через Пифагора
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        # Выводим результат
        print(result)

#Проверка "точки входа"
if __name__ == '__main__':
    # Запоминаем текущее время
    start_time = datetime.now()
    # Вызываем функцию main, передавая ей несколько именованных аргументов.
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )
    # Вычисляем продолжительность выполнения программы, вычитая начальное время из текущего.
    time_costs = datetime.now() - start_time
    # Выводим на экран время выполнения программы.
    print(f"Время выполнения программы - {time_costs}")
```
### Результат.
![1 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_4/pic/4.11.png)

## Выводы.

Изначальный код был задокументирован. Вкратце, код высчитывает расстояние между векторами методом Пифагора, и высчитывает и выводит время вычислений.

## Самостоятельная работа №2
### Напишите программу, которая будет заменять игральную кость с 6 гранями. Если значение равно 5 или 6, то в консоль выводится «Вы победили», если значения 3 или 4, то вы рекурсивно должны вызвать эту же функцию, если значение 1 или 2, то в консоль выводится «Вы проиграли». При этом каждый вызов функции необходимо выводить в консоль значение “кубика”. Для выполнения задания необходимо Михаил А. Панов использовать стандартную библиотеку random. Программу нужно написать, используя одну функцию и “точку входа”

```python
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
```
### Результат.
![2 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_4/pic/4.12.png)

## Выводы.

Программа рандомно имитирует кубик, рандомно генерируя случайное число от 1 до 6. В зависимости от выпавшего числа выводится определенное сообщение или запускается рекурсия.

## Самостоятельная работа №3
### Напишите программу, которая будет выводить текущее время, с точностью до секунд на протяжении 5 секунд. Программу нужно написать с использованием цикла. Подсказка: необходимо использовать модуль datetime и time, а также вам необходимо как-то “усыплять” программу на 1 секунду

```python
import time

def funtime():
    for o in range(5):
        current_time = time.strftime("%H:%M:%S")
        print("Текущее время:", current_time)
        time.sleep(1)


if __name__ == '__main__':
    funtime()
```
### Результат.
![3 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_4/pic/4.13.png)

## Выводы.

Программа выводит текущее время (С точностью до секунды). При помощи time.sleep программа выводит время каждую секунду.  

## Самостоятельная работа №4
###  Напишите программу, которая считает среднее арифметическое от аргументов вызываемое функции, с условием того, что изначальное количество этих аргументов неизвестно. Программу необходимо реализовать используя одну функцию и “точку входа”.

```python
def median(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

if __name__ == '__main__':
    result = median(1,2,3,4,5,6,7,8,9,10)
    print(f"Среднее арифметическое = {result}")
```
### Результат.
![4 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_3/pic/3.14.png)

## Выводы.

Программа на вход получает ряд неповторяющихся чисел (Неизвестно сколько их изначально). В функции median высчитывается среднее арифметическое. Если аргументов 0, то выводится соответствующее сообщение.

## Самостоятельная работа №5
### Создайте два Python файла, в одном будет выполняться вычисление площади треугольника при помощи формулы Герона (необходимо реализовать через функцию), а во втором будет происходить взаимодействие с пользователем (получение всей необходимой информации и вывод результатов). Напишите эту программу и выведите в консоль полученную площадь.

```python
import math

def geronfun(a,b,c):
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s
```
```python
from Ind4_5_1 import geronfun

def main():
    print('Введите длины сторон')
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))

    print(f"Площадь = {geronfun(a,b,c)}")

if __name__ == '__main__':
    main()
```
### Результат.
![5 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_4/pic/4.15_1.png)
![5 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_4/pic/4.15_2.png)

## Выводы.

В первом файле написана логика кода. P - полупериметр, S - площадь, посчитанная методом Герона (Формула подразумевает использование квадратного корня. Он был использован из библиотеки math). Во втором файле используются функции input, чтобы пользователь вводил длины сторон треугольника, после чего выводится площадь треугольника.

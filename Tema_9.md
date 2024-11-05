# Тема 8. Введение в ООП
Отчем по теме #8 выполнил(а):
- Клейн Денис Романович
- АИС-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | - | - |
| Задание 7 | - | - |
| Задание 8 | - | - |
| Задание 9 | - | - |
| Задание 10 | - | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python 
#Создание класса
class Car:
    #Определение конструктора
    def __init__(self, make, model):
        #Определение атрибутов
        self.make = make
        self.model = model
#Создание экземпляра класса
my_car = Car("Toyota", "Corolla")
```

### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_8/pic/1.png)

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
#Создание класса
class Car:
    #Определение конструктор
    def __init__(self, make, model):
        #Определение атрибутов
        self.make = make
        self.model = model

    #Создание метода, который выводит информацию в консоль
    def drive(self):
        print(f"Driving the {self.make} {self.model}")

#Создание экземпляра класса
my_car = Car("Toyota", "Corolla")
#Вызов метода
my_car.drive()
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_8/pic/2.png)

## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
#Создание класса
class Car:
    #Определение конструктора
    def __init__(self, make, model):
        #Определение атрибутов
        self.make = make
        self.model = model

    #Создание метода, который выводит информацию в консоль
    def drive(self):
        print(f"Driving the {self.make} {self.model}")

#Создание экземпляра класса
my_car = Car("Toyota", "Corolla")
#Вызов метода
my_car.drive()

#Создание класса
class ElectricCar(Car):
    #Определение конструктора
    def __init__(self, make, model, battery_capacity):
        #Вызов конструктора родительского класса
        super().__init__(make,model)
        #Определение атрибута
        self.battery_capacity = battery_capacity
    #Создание метода зарядки
    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")
#Создание экземпляра класса
my_electric_car = ElectricCar("Tesla", "Model S", 75)
#Вызов метода drive() и charge()
my_electric_car.drive()
my_electric_car.charge()
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_8/pic/3.png)

## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
#Создание класса
class Car:
    #Определение конструктор
    def __init__(self, make, model):
        #Определение атрибутов
        self._make = make
        self.__model = model

    #Создание метода, который выводит информацию в консоль
    def drive(self):
        print(f"Driving the {self._make} {self.__model}")

#Создание экземпляра класса
my_car = Car("Toyota", "Corolla")
#Доступ к защищенному атрибуту
print(my_car._make)
#__model вызовет ошибку, т.к. он приветный
#Вызов метода drive()
my_car.drive()
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_8/pic/4.png)

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    # Метод инициализации класса
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Метод для подсчета площади фигуры
    def area(self):
        return self.width * self.height

class Circle(Shape):
    # Метод инициализации класса
    def __init__(self, radius):
        self.radius = radius

    # Метод для подсчета площади фигуры
    def area(self):
        return 3.14 * self.radius * self.radius

# Список
arr = [Rectangle(2, 2), Circle(4)]
# Вызов метода area
for elem in arr:
    print(elem.area())
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_8/pic/5.png)

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
#Создание класса
class Food:
    #Определение конструктора
    def __init__(self, name, calorie, price):
        self.name = name
        self.calorie = calorie
        self.price = price
#Создание экземпляра класса
milk = Food("milk",58, 100)
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_8/pic/6.png)

## Выводы.
В данном коде создан класс Food с атрибутами name, calorie и price. 

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
#Создание класса
class Food:
    #Определение конструктора
    def __init__(self, name, calorie, price):
        self.name = name
        self.calorie = calorie
        self.price = price

    # Метод, который выводит информацию в консоль
    def showinfo(self):
        print(f"Название: {self.name}, Калорийность: {self.calorie}, Цена: {self.price}")

    def eat(self):
        pass

#Создание экземпляра класса
milk = Food("milk",58, 100)
#Вызов функции showinfo()
milk.showinfo()
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_8/pic/7.png)

## Выводы.
В данном коде создан класс Food с атрибутами name, calorie и price. Также есть 2 метода (showinfo() и eat()). showinfo выводит информацию.

## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
#Создание класса
class Food:
    #Определение конструктора
    def __init__(self, name, calorie, price):
        self.name = name
        self.calorie = calorie
        self.price = price

    # Метод, который выводит информацию в консоль
    def showinfo(self):
        print(f"Название: {self.name}, Калорийность: {self.calorie}, Цена: {self.price}")

    def eat(self):
        pass
#Создание класса fpc (Ftas, Protein, Carbs)
class Fpc(Food):
    def __init__(self, name, calorie, price, fats, protein, carbs):
        # Вызов конструктора родительского класса
        super().__init__(name, calorie, price)
        self.fats = fats
        self.protein = protein
        self.carbs = carbs

    # Метод, который выводит информацию в консоль
    def showtopic(self):
        print(f"Название: {self.name}, Калорийность: {self.calorie}, Цена: {self.price}\n жиры: {self.fats}, белки: {self.protein}, углеводы: {self.carbs}")

#Создание экземпляра класса
milk = Food("milk",58, 100)
#Вызов функции showinfo()
milk.showinfo()

#Создание экземпляра класса Fpc
meat = Fpc("Meat", 230, 780, 18, 16,0)
#Вызов функции showtopic()
meat.showtopic()
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_8/pic/8.png)

## Выводы.
В данном коде создан класс Food с атрибутами name, calorie и price. Класс Food является родительским для класса Fpc с атрибутами fats, protein и carbs. Также создаются атрибуты milk и meat.

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
#Создание класса
class Food:
    #Определение конструктора
    def __init__(self, name, calorie, price):
        self.name = name
        self._calorie = calorie
        self.__price = price

    # Метод, который выводит информацию в консоль
    def showinfo(self):
        print(f"Название: {self.name}, Калорийность: {self._calorie}, Цена: {self.__price}")

    def eat(self):
        pass

#Создание экземпляра класса
milk = Food("milk",58, 100)
milk._calorie = 60
#__price не изменится, т.к. атрибут приватный.
milk.__price = 120
#Вызов функции showinfo()
milk.showinfo()
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_8/pic/9.png)

## Выводы.
В данном коде реализована инкапсуляция. В классе Food есть защищенный _calorie и приватный __price. После создается milk и выводится информация о нём.

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
#Создание класса
class Food:
    def info(self):
        pass

class Fats(Food):
    # Метод инициализации класса
    def __init__(self, fats):
        self.fats = fats

    # Вывод информации
    def info(self):
        print(f"Жиры {self.fats}")


class Protein(Food):
    # Метод инициализации класса
    def __init__(self, protein):
        self.protein = protein
    # Вывод информации
    def info(self):
        print(f"Белки {self.protein}")


class Carbs(Food):
    # Метод инициализации класса
    def __init__(self, carbs):
        self.carbs = carbs
    # Вывод информации
    def info(self):
        print(f"Углеводы {self.carbs}")

meat = [Fats(10), Protein(20), Carbs(30)]
for food in meat:
    food.info()
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_8/pic/10.png)

## Выводы.
В данном коде реализован полиморфизм с использованием основного класса Food и классов Fats, Protein и Carbs. Они имеют общий метод info (выводит информацию). В зависимости от класса метод переопределяется. После создается список с объектами классов и для каждого из них вызывается метод info.


# Тема 9. Концепции и принципы ООП.
Отчем по теме #9 выполнил(а):
- Клейн Денис Романович
- АИС-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | - |
| Задание 3 | + | - |
| Задание 4 | + | - |
| Задание 5 | + | - |
| Задание 6 | - | - |
| Задание 7 | - | - |
| Задание 8 | - | - |
| Задание 9 | - | - |
| Задание 10 | - | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Допустим, что вы решили оригинально и немного странно познакомится с человеком. Для этого у вас должен быть написан свой класс на Python, который будет проверять угадал ваше имя человек или нет. Для этого создайте класс, указав в свойствах только имя. Дальше создайте функцию init(), а в ней сделайте проверку на то угадал человек ваше имя или нет. Также можете проверить что будет, если в этой функции указав атрибут, который не указан в вашем классе, например, попробуйте вызвать фамилию.

```python 
class Ivan:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Иван':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, я Иван"

person1 = Ivan('Алексей')
person2 = Ivan('Иван')

print(person1.name)
print(person2.name)
```

### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_9/pic/1.png)

## Лабораторная работа №2
### Вам дали важное задание, написать продавцу мороженого программу, которая будет писать добавили ли топпинг в мороженое и цену после возможного изменения. Для этого вам нужно написать класс, в котором будет определяться изменили ли состав мороженого или нет. В этом классе реализуйте метод, выводящий на печать «Мороженое с {ТОППИНГ}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое». При этом программа должна воспринимать как топпинг только атрибуты типа string.

```python
class Icecream:
    def __init__(self, ingredient = None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def composition(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient}")
        else:
            print("Обычное мороженое")

icecream = Icecream()
icecream.composition()
icecream = Icecream("шоколадом")
icecream.composition()
icecream = Icecream(5)
icecream.composition()
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_9/pic/2.png)

## Лабораторная работа №3
### Петя – начинающий программист и на занятиях ему сказали реализовать икапсу…что-то. А вы хороший друг Пети и ко всему прочему прекрасно знаете, что икапсу…что-то – это инкапсуляция, поэтому решаете помочь вашему другу с написанием класса с инкапсуляцией. Ваш класс будет не просто инкапсуляцией, а классом с сеттером, геттером и деструктором. После написания класса вам необходимо продемонстрировать что все написанные вами функции работают. Также вам необходимо объяснить Пете почему на скриншоте ниже в консоли выводится ошибка.

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def del_value(self):
        del self._value

    value = property(get_value, set_value, del_value, "Свойство value")

example = MyClass(30)
print(example.get_value())
example.set_value(50)
print(example.get_value())
example.set_value(100)
print(example.get_value())
example.del_value()
#Возникает ошибка, т.к. _value был удален методом del_value, а затем код пытается к нему обратиться через гетер.
print(example.get_value())
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_9/pic/3.png)

## Лабораторная работа №4
### Вам прекрасно известно, что кошки и собаки являются млекопитающими, но компьютер этого не понимает, поэтому вам нужно написать три класса: Кошки, Собаки, Млекопитающие. И при помощи “наследования” объяснить компьютеру что кошки и собаки – это млекопитающие. Также добавьте какой-нибудь свой атрибут для кошек и собак, чтобы показать, что они чем-то отличаются друг от друга.

```python
class Mammal:
    className = "Mammal"

class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'

class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'

dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds}")
cat = Cat()
print(f"Cat is {cat.className}, but they say {cat.sounds}")
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_9/pic/4.png)

## Лабораторная работа №5
### На разных языках здороваются по-разному, но суть остается одинаковой, люди друг с другом здороваются. Давайте вместе с вами реализуем программу с полиморфизмом, которая будет описывать всю суть первого предложения задачи. Для этого мы можем выбрать два языка, например, русский и английский и написать для них отдельные классы, в которых будет в виде атрибута слово, которым здороваются на этих языках. А также напишем функцию, которая будет выводить информацию о том, как на этих языках здороваются. Заметьте, что для решения поставленной задачи мы использовали декоратор @staticmethod, поскольку нам не нужны обязательные параметры-ссылки вроде self.

```python
class Russian:
    @staticmethod
    def greeting():
        print("Привет")

class English:
    @staticmethod
    def greeting():
        print("Hello")

def greet(language):
    language.greeting()

ivan = Russian()
greet(ivan)
john = English()
greet(john)
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_9/Lab9_5.py)

## Самостоятельная работа №1
### Садовник и помидоры.

```python
class Tomato:
    #Словарь состояний помидоров #
    states = ['Отсутствие','Цветение','Зеленый','Красный']

    #Инициализация Tomato, Index - Индекс (номер) томата, state - состояние (рост) томата.
    def __init__(self, index):
        self.index = index
        self._state = 0

    #Метод для увеличения стадии роста томата.
    def grow(self):
        self._state=self._state + 1

    #Проверка стадии роста томата.
    def is_ripe(self):
        return self._state == 3

class TomatoBush:
    #Инициализация TomatoBush. num_tomato - кол-во томатов на кусте, tomatoes - список томатов на кусте.
    def __init__(self, num_tomato):
        self.tomatoes = [Tomato(index) for index in range (0, num_tomato)]

    #Увеличивает стадию роста на 1.
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    #Проверяет стадию роста у всех томатов на кусте
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    #Очистка куста (списка) от томатов.
    def give_away_all(self):
        self.tomatoes.clear()

class Gardener:
    #Инициализация Gardener. name - имя садовника, plant - куст томатов.
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    #Увеличивает стадию роста всех томатов на 1.
    def work(self):
        self._plant.grow_all()
        print("Садовник работает...")

    #Сбор урожая (всех зрелых помидоров) с куста
    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Собрано")
        else:
            print("Не созрели")

    #Вывод руководства
    @staticmethod
    def knowledge_base():
        print("===РУКОВОДСТВО===\n1 - Посадить кусты с помидорами\n2 - Заставить садовника работать\n3 - Ухаживать за кустом\n4 - Собрать помидоры")

#Создание куста с 5 помидорами
bush = TomatoBush(5)
#Создание садовника
gardener = Gardener("Серега", bush)
#Вызов справки
Gardener.knowledge_base()

gardener.work()
gardener.harvest()

gardener.work()
gardener.work()
gardener.harvest()
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_9/pic/6.png)

## Выводы.
В данном коде реализованы классы, в которых реализован процесс ухода за кустом с помидорами. Класс Tomato - отвечает за каждый единичный помидор (Его рост и стадия созревания), TomatoBush - за куст, на котором растут помидоры, Gardener - за садовника, который ухаживает за кустом с помидорами, а также может собирать урожай. Также реализовано руковосдтво, которое можно вызвать. В конце реализованы методы, которые тестируют код на работоспособность. 


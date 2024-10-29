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
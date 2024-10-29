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
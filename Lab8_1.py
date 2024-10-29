#Создание класса
class Car:
    #Определение конструктора
    def __init__(self, make, model):
        #Определение атрибутов
        self.make = make
        self.model = model
#Создание экземпляра класса
my_car = Car("Toyota", "Corolla")
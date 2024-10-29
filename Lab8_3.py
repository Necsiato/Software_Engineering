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
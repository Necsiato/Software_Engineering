#Создание класса
class Food:
    #Определение конструктора
    def __init__(self, name, calorie, price):
        self.name = name
        self.calorie = calorie
        self.price = price
#Создание экземпляра класса
milk = Food("milk",58, 100)
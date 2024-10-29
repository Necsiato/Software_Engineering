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
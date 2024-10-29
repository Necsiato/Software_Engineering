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
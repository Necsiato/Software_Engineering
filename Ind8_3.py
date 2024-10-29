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
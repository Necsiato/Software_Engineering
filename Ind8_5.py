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
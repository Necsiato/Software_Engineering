class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    # Метод инициализации класса
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # Метод для подсчета площади фигуры
    def area(self):
        return self.width * self.height

class Circle(Shape):
    # Метод инициализации класса
    def __init__(self, radius):
        self.radius = radius

    # Метод для подсчета площади фигуры
    def area(self):
        return 3.14 * self.radius * self.radius

# Список
arr = [Rectangle(2, 2), Circle(4)]
# Вызов метода area
for elem in arr:
    print(elem.area())
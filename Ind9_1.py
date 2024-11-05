class Tomato:
    #Словарь состояний помидоров #
    states = ['Отсутствие','Цветение','Зеленый','Красный']

    #Инициализация Tomato, Index - Индекс (номер) томата, state - состояние (рост) томата.
    def __init__(self, index):
        self.index = index
        self._state = 0

    #Метод для увеличения стадии роста томата.
    def grow(self):
        self._state=self._state + 1

    #Проверка стадии роста томата.
    def is_ripe(self):
        return self._state == 3

class TomatoBush:
    #Инициализация TomatoBush. num_tomato - кол-во томатов на кусте, tomatoes - список томатов на кусте.
    def __init__(self, num_tomato):
        self.tomatoes = [Tomato(index) for index in range (0, num_tomato)]

    #Увеличивает стадию роста на 1.
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    #Проверяет стадию роста у всех томатов на кусте
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    #Очистка куста (списка) от томатов.
    def give_away_all(self):
        self.tomatoes.clear()

class Gardener:
    #Инициализация Gardener. name - имя садовника, plant - куст томатов.
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    #Увеличивает стадию роста всех томатов на 1.
    def work(self):
        self._plant.grow_all()
        print("Садовник работает...")

    #Сбор урожая (всех зрелых помидоров) с куста
    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Собрано")
        else:
            print("Не созрели")

    #Вывод руководства
    @staticmethod
    def knowledge_base():
        print("===РУКОВОДСТВО===\n1 - Посадить кусты с помидорами\n2 - Заставить садовника работать\n3 - Ухаживать за кустом\n4 - Собрать помидоры")

#Создание куста с 5 помидорами
bush = TomatoBush(5)
#Создание садовника
gardener = Gardener("Серега", bush)
#Вызов справки
Gardener.knowledge_base()

gardener.work()
gardener.harvest()

gardener.work()
gardener.work()
gardener.harvest()

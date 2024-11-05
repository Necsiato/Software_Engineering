class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def del_value(self):
        del self._value

    value = property(get_value, set_value, del_value, "Свойство value")

example = MyClass(30)
print(example.get_value())
example.set_value(50)
print(example.get_value())
example.set_value(100)
print(example.get_value())
example.del_value()
#Возникает ошибка, т.к. _value был удален методом del_value, а затем код пытается к нему обратиться через гетер.
print(example.get_value())
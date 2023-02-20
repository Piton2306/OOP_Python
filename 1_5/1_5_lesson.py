# _имя магического метода
# __init__(self) - инициализатор объекта
# __del__(self) - финализатор класса

class Point:
    color = 'red'  # свойства данные
    circle = 2

    def __init__(self, x=0, y=0):
        print("Вызов __init__")
        self.x = x
        self.y = y

    def __del__(self):
        print("Удаление")

    def set_coords(self):  # Методы-набор координат
        self.x = x
        self.y = y

    def get_coords(self):  # Получить координаты
        return self.x, self.y


pt = Point(1, 2)
# pt.set_coords(4, 4)
print(pt.__dict__)
print(pt.get_coords())

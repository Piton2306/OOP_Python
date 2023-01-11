"""1.4 Методы классов. Параметр self"""


class Point:
    color = 'red'  # свойства данные
    circle = 2

    def set_coords(self, x, y):  # Методы
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


pt = Point()
pt.set_coords(4, 4)
print(pt.get_coords())

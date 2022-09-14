"""1.3 Классы и объекты. Атрибуты классов и объектов"""


class Point:
    """Документация класса"""
    color = 'red'  # атрибут класса или его свойства
    circle = 2


a = Point()  # Создание нового класса от класса Point
setattr(a, "colors", "blue")  # Задаёт значение атрибута
delattr(a, 'colors')  # Удаляет атрибут с именем
print(Point.__dict__)  # Вывод всех атрибутов класса
print(Point.__doc__)  # вывод документации
print(getattr(Point, "color"))  # Возвращает значение атрибута
print(hasattr(Point, "color"))  # Проверяет наличие атрибута класса
print(getattr(Point, "color"))

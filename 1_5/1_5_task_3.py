from random import randint


class Line:  # линия
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:  # прямой
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:  # еллипс
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = [(Line, Rect, Ellipse)[randint(0, 2)](1, 2, 3, 4) for n in range(217)]

for obj in elements:
    if isinstance(obj, Line):
        obj.sp = obj.ep = 0, 0

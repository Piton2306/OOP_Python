class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        a, b, c = self.a, self.b, self.c
        for i in a, b, c:
            if str(type(i))[8:-2] not in ['int', 'float'] or i <= 0:
                print(a, b, c)
                return 1
        if a + b <= c or a + c <= b or c + b <= a:
            return 2
        return 3


a, b, c = map(int, '3 4 -1'.split())

tr = TriangleChecker(a, b, c)
tr.is_triangle()

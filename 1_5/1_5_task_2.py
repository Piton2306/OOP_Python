class Point:

    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color


points = [Point(i, i) for i in range(1, 2000, 2)]
points[1] = Point(3, 3, 'yellow')
#
# for i in range(3, 2000, 2):
#     points.append(Point(i, i))
print(points)
points1 = [tuple(points[i].__dict__.values()) for i in range(1000)]
print(len(points))
print(points1)
print(len(points1))

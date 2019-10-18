class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def print_point(self):
        print(self.x, self.y, self.z)


p1 = Point(2, 3, 5)
p1.print_point()

p2 = Point(5, 7, -1)
p2.print_point()

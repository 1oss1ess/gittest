class Point:
    def assign(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def print_point(self):
        print(self.x, self.y, self.z)


p1 = Point()
p1.assign(2, 3, 5)
p1.print_point()

p2 = Point()
p2.assign(5, 7, -1)
p2.print_point()

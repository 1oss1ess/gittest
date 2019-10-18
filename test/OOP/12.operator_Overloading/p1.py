class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return('({0}, {1}, {2})'.format(self.x, self.y, self.z))

    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        self.z = self.z + other.z
        return Point(self.x, self.y, self.z)


def main():
    p1 = Point(5, 1, 9)
    print(p1)
    p2 = Point(3, 4, 7)
    print(p2)
    print(p1 + p2)


if __name__ == '__main__':
    main()

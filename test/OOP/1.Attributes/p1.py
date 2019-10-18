class Test1:
    pass


class Point:
    pass


p1 = Point()
p1.x = 2
p1.y = 3
p1.z = 5

p2 = Point()
p2.x = 5
p2.y = 7
p2.z = -1

print(p1)
print(p1.x, p1.y, p1.z)

print(p2)
print(p2.x, p2.y, p2.z)

t1 = Test1()
t1.text = 'Hello World!'

print(t1)
print(t1.text)

t1.var = 3.14

print(t1.var)

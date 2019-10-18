class Muffin:
    amount = 0

    def __init__(self, color, taste, calories):
        self.color = color
        self.taste = taste
        self.calories = calories


yummy = Muffin('brown', 'sweet', 420)
# print(yummy.__dict__)
# print(yummy.amount)
# print(yummy.__dict__)

yummy.color = 'White'
yummy.price = 5
print(yummy.__dict__)
del yummy.price
print(yummy.__dict__)
print(hasattr(yummy, 'color'))
print(hasattr(yummy, 'price'))
print(getattr(yummy, 'color'))
print(getattr(yummy, 'price', None))
print(getattr(yummy, 'price', 1000000))
print(yummy.__dict__)
setattr(yummy, 'price', 430)
print(yummy.__dict__)
print(getattr(yummy, 'amount'))

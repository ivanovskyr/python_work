class Rectangle:        # Класс для определения площади прямоугольника
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def getArea(self):
        return self.a*self.b

class Square:            # Класс для определения площади квадрата
    def __init__(self, a):
        self.a = a
    def getAreaSquare(self):
        return self.a**2

class Circle:           # Класс для определения площади круга
    def __init__(self, r):
        self.r = r
    def getAreaCircle(self):
        return 3.14*self.r**2
from practice import Rectangle,Square, Circle
# Задаем и выводим площадь прямоугольников
rect_1 = Rectangle(3, 4)
rect_2 = Rectangle(12, 5)

print(rect_1.getArea())
print(rect_2.getArea())

# Задаем и выводим площадь квадратов
square_1 = Square(5)
square_2 = Square(10)

print(square_1.getAreaSquare(),
      square_2.getAreaSquare())

# Задаем и выводим площадь круга через радиус
circle_1 =Circle(5)
circle_2 =Circle(10)

print(circle_1.getAreaCircle(),
      circle_2.getAreaCircle())

# Собираем все фигуры в единую коллекцию
figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.getAreaSquare())
    elif isinstance(figure, Circle):
        print(figure.getAreaCircle())
    else:
        print(figure.getArea())
# # Задание 16.9.1
# # Создайте класс одной из геометрических фигур (например, прямоугольника),
# # где в конструкторе задаются атрибуты:  начальные координаты x, y, width и height
# # (или другие в зависимости от выбранной фигуры).
# # Создайте метод, который возвращает атрибуты прямоугольника как строку ( постарайтесь применить магический метод __str__).
# # Для объекта прямоугольника со значениями атрибута x = 5, y = 10, width = 50, height = 100 метод должен вернуть
# # строку Rectangle : 5, 10, 50, 100.
#
# class Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return f'Прямоугольник: \n' \
#                f'по X: {self.x}\n' \
#                f'по Y: {self.y}\n' \
#                f'ширина: {self.width}\n' \
#                f'высота: {self.height}'
#
# x1 = Rectangle(5, 10, 50, 100)
# print(x1)


# Задание 16.9.2
# Напишите код для описания геометрической фигуры.
# Создайте класс «прямоугольник» с помощью метода init().
# На выходе в консоли вам необходимо получить площадь данной фигуры.

# class  Rectangle:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#     def __str__(self):
#         return f'Координаты прямоугольника: {self.x}:{self.y}, ширина * высота: {self.width} * {self.height}'
#     def getArea(self):
#         return f'Площадь прямоугольника = {self.width*self.height}'
#
# rect_2 = Rectangle(4, 7, 10, 25)
# print(rect_2.__str__())
# print(rect_2.getArea())

# Задание 16.9.3
# В проекте «Дом питомца» добавим новую услугу — электронный кошелек.
# Необходимо создать класс «Клиент», который будет содержать данные о клиентах и их финансовых операциях.
# О клиенте известна следующая информация: имя, фамилия, город, баланс.
# Далее сделайте вывод о клиентах в консоль в формате:
# «Иван Петров. Москва. Баланс: 50 руб.»

# class Client:
#     def __init__(self, name, family, city, balans):
#         self.name = name
#         self.family = family
#         self.city = city
#         self.balans = balans
#     def __str__(self):
#         return f'{self.name} {self.family}. {self.city}. Баланс: {self.balans} руб.'
#
# stepanov = Client(name='Андрей', family='Степанов', city='Владивосток', balans='5382')
# osipov = Client(name='Валерий', family='Осипов', city='Малая Сазанка', balans='14593')
# print(stepanov)


# Задание 16.9.4
# Команда проекта «Дом питомца» планирует большой корпоратив для своих клиентов.
# Вам необходимо написать программу, которая позволит составить список гостей.
# В класс «Клиент» добавьте метод, который будет возвращать информацию только об имени, фамилии и городе клиента.
# Затем создайте список, в который будут добавлены все клиенты, и выведете его в консоль.


class Client:
    def __init__(self, name, family, city, balans):
        self.name = name
        self.family = family
        self.city = city
        self.balans = balans
    def __str__(self):
        return f'{self.name} {self.family}. {self.city}. Баланс: {self.balans} руб.'
    def party(self):
        return f'{self.name} {self.family}. {self.city}'


stepanov = Client(name='Андрей', family='Степанов', city='Владивосток', balans='5382')
osipov = Client(name='Валерий', family='Осипов', city='Малая Сазанка', balans='14593')
solovei = Client(name='Олег', family='Соловей', city='Хабаровск', balans='11000')

guests = [stepanov, osipov, solovei]

for guest in guests:
    print(guest.party())


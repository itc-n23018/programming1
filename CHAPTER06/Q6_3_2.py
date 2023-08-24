class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


rectangle = Rectangle(4, 3)
print("長方形の周の長さ:", rectangle.calculate_perimeter())
print("長方形の面積:", rectangle.calculate_area())

square = Square(4)
print("正方形の周の長さ:", square.calculate_perimeter())
print("正方形の面積:", square.calculate_area())

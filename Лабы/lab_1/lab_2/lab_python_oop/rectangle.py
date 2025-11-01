from .figure import Figure
from .color import Color


class Rectangle(Figure):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height}, color={self.color.color})"
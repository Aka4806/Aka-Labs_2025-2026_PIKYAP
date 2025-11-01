from .figure import Figure
from .color import Color
import math

class Circle(Figure):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"Circle(radius={self.radius}, color={self.color.color})"
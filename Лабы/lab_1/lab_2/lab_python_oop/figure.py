from abc import ABC, abstractmethod
from .color import Color


class Figure(ABC):
    def __init__(self, color):
        self.color = color if isinstance(color, Color) else Color(color)

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(color={self.color.color})"
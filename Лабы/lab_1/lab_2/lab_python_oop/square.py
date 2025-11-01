from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side, color):
        super().__init__(side, side, color)
        self.side = side

    def __repr__(self):
        return f"Square(side={self.side}, color={self.color.color})"
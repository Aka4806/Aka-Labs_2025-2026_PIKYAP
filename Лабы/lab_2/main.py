from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    rectangle = Rectangle(10, 10, "синий")
    circle = Circle(10, "зеленый")
    square = Square(10, "красный")

    # Вывод информации о фигурах
    print("Информация о фигурах:")

    print(f"Прямоугольник: {rectangle}")
    print(f"Площадь: {rectangle.area()}")
    print(f"Периметр: {rectangle.perimeter()}")
    print()

    print(f"Круг: {circle}")
    print(f"Площадь: {circle.area():.2f}")
    print(f"Длина окружности: {circle.perimeter():.2f}")
    print()

    print(f"Квадрат: {square}")
    print(f"Площадь: {square.area()}")
    print(f"Периметр: {square.perimeter()}")
    print()

    # Демонстрация полиморфизма
    figures = [rectangle, circle, square]

    print("Демонстрация полиморфизма:")
    for figure in figures:
        area = figure.area()
        perimeter = figure.perimeter()
        if isinstance(figure, Circle):
            print(f"{figure.__class__.__name__}: площадь = {area:.2f}, периметр = {perimeter:.2f}")
        else:
            print(f"{figure.__class__.__name__}: площадь = {area}, периметр = {perimeter}")


if __name__ == "__main__":
    main()
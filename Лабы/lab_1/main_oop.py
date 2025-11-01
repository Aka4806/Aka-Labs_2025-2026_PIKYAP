import sys

class EquationSolver:

    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
        self.roots = []

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Коэффициент A должен быть числом")
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Коэффициент B должен быть числом")
        self._b = value

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Коэффициент C должен быть числом")
        self._c = value

    def solve_linear_case(self):
        if self.c == 0:
            return ["Все действительные числа"]
        else:
            return []

    def solve_quadratic_case(self):
        roots = []
        x_squared = -self.c / self.b

        if x_squared > 0:
            x1 = x_squared ** 0.5
            x2 = -x1
            roots.extend([x1, x2])
        elif x_squared == 0:
            roots.append(0.0)

        return roots

    def solve_biquadratic_case(self):
        roots = []
        discriminant = self.b ** 2 - 4 * self.a * self.c

        if discriminant < 0:
            return []
        elif discriminant == 0:
            y = -self.b / (2 * self.a)
            if y > 0:
                x1 = y ** 0.5
                x2 = -x1
                roots.extend([x1, x2])
            elif y == 0:
                roots.append(0.0)
        else:
            y1 = (-self.b + discriminant ** 0.5) / (2 * self.a)
            y2 = (-self.b - discriminant ** 0.5) / (2 * self.a)

            for y in [y1, y2]:
                if y > 0:
                    x1 = y ** 0.5
                    x2 = -x1
                    roots.extend([x1, x2])
                elif y == 0:
                    roots.append(0.0)

        return sorted(list(set(roots)))

    def solve(self):
        self.roots = []

        if self.a == 0:
            if self.b == 0:
                self.roots = self.solve_linear_case()
            else:
                self.roots = self.solve_quadratic_case()
        else:
            self.roots = self.solve_biquadratic_case()

        return self.roots

    def display_solution(self):
        print(f"\nУравнение: {self.a}x⁴ + {self.b}x² + {self.c} = 0")

        if self.a == 0:
            if self.b == 0:
                print("Уравнение линейное")
            else:
                print("Уравнение квадратное (A = 0)")
        else:
            discriminant = self.b ** 2 - 4 * self.a * self.c
            print(f"Дискриминант: {discriminant}")

        if not self.roots:
            print("Действительных корней нет")
        elif self.roots == ["Все действительные числа"]:
            print("Уравнение превращается в тождество: 0 = 0")
            print("Решение: все действительные числа")
        else:
            roots_str = ", ".join([f"x{i + 1} = {root:.4f}" for i, root in enumerate(self.roots)])
            print(f"Корни: {roots_str}")


class InputHandler:

    @staticmethod
    def is_valid_float(value):
        try:
            float(value)
            return True
        except (ValueError, TypeError):
            return False

    @staticmethod
    def get_coefficient(prompt, param_value=None):
        while True:
            if param_value is not None and InputHandler.is_valid_float(param_value):
                value = float(param_value)
                print(f"{prompt} = {value}")
                return value
            else:
                user_input = input(prompt)
                if InputHandler.is_valid_float(user_input):
                    return float(user_input)
                print("Ошибка: введите действительное число")

def main():
    print("Решение уравнения Ax⁴ + Bx² + C = 0")

    # Получаем коэффициенты из параметров командной строки или с клавиатуры
    a_param = sys.argv[1] if len(sys.argv) > 1 else None
    b_param = sys.argv[2] if len(sys.argv) > 2 else None
    c_param = sys.argv[3] if len(sys.argv) > 3 else None

    a = InputHandler.get_coefficient("Введите коэффициент A: ", a_param)
    b = InputHandler.get_coefficient("Введите коэффициент B: ", b_param)
    c = InputHandler.get_coefficient("Введите коэффициент C: ", c_param)

    try:
        equation = EquationSolver(a, b, c)
        equation.solve()
        equation.display_solution()
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
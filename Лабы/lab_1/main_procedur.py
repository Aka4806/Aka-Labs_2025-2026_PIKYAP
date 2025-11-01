import sys

def is_valid_float(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def get_coefficient(prompt, param_value=None):
    while True:
        if param_value is not None and is_valid_float(param_value):
            value = float(param_value)
            print(f"{prompt} = {value}")
            return value
        else:
            user_input = input(prompt)
            if is_valid_float(user_input):
                return float(user_input)
            print("Ошибка: введите действительное число")

def solve_equation(a, b, c):
    print(f"\nУравнение: {a}x⁴ + {b}x² + {c} = 0")

    roots = []

    if a == 0:
        if b == 0:
            if c == 0:
                print("Уравнение превращается в тождество: 0 = 0")
                return ["Все действительные числа"]
            else:
                print(f"Уравнение не имеет решений: {c} = 0")
                return []
        else:
            print("Уравнение квадратное (A = 0)")
            x_squared = -c / b

            if x_squared > 0:
                x1 = x_squared ** 0.5
                x2 = -x1
                roots.extend([x1, x2])
                print(f"Корни: x₁ = {x1:.4f}, x₂ = {x2:.4f}")
            elif x_squared == 0:
                roots.append(0.0)
                print(f"Корень: x = 0.0")
            else:
                print("Действительных корней нет")
            return roots
    else:
        discriminant = b ** 2 - 4 * a * c
        print(f"Дискриминант: {discriminant}")

        if discriminant < 0:
            print("Действительных корней нет")
        elif discriminant == 0:
            y = -b / (2 * a)
            if y > 0:
                x1 = y ** 0.5
                x2 = -x1
                roots.extend([x1, x2])
                print(f"Корни: x₁ = {x1:.4f}, x₂ = {x2:.4f}")
            elif y == 0:
                roots.append(0.0)
                print(f"Корень: x = 0.0")
            else:
                print("Действительных корней нет")
        else:                                      #  y=x^2
            y1 = (-b + discriminant ** 0.5) / (2 * a)
            y2 = (-b - discriminant ** 0.5) / (2 * a)

            for y in [y1, y2]:
                if y > 0:
                    x1 = y ** 0.5
                    x2 = -x1
                    roots.extend([x1, x2])
                elif y == 0:
                    roots.append(0.0)

            roots = sorted(list(set(roots)))

            if roots:
                roots_str = ", ".join([f"x{i + 1} = {root:.4f}" for i, root in enumerate(roots)])
                print(f"Корни: {roots_str}")
            else:
                print("Действительных корней нет")

    return roots

def main():
    print("Решение уравнения Ax⁴ + Bx² + C = 0")

    a_param = sys.argv[1] if len(sys.argv) > 1 else None
    b_param = sys.argv[2] if len(sys.argv) > 2 else None
    c_param = sys.argv[3] if len(sys.argv) > 3 else None

    a = get_coefficient("Введите коэффициент A: ", a_param)
    b = get_coefficient("Введите коэффициент B: ", b_param)
    c = get_coefficient("Введите коэффициент C: ", c_param)

    solve_equation(a, b, c)

if __name__ == "__main__":
    main()
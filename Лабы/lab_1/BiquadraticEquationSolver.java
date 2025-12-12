import java.util.*;

public class BiquadraticEquationSolver {
    public static void main(String[] args) {
        System.out.println("Решение уравнения Ax⁴ + Bx² + C = 0");
        System.out.println("=".repeat(50));
        System.out.println("Все коэффициенты A, B, C могут быть равны 0");

        InputHandler inputHandler = new InputHandler();
        double a = inputHandler.getCoefficient("Введите коэффициент A: ", args.length > 0 ? args[0] : null);
        double b = inputHandler.getCoefficient("Введите коэффициент B: ", args.length > 1 ? args[1] : null);
        double c = inputHandler.getCoefficient("Введите коэффициент C: ", args.length > 2 ? args[2] : null);

        try {
            Equation equation = new Equation(a, b, c);
            equation.solve();
            equation.displaySolution();
        } catch (IllegalArgumentException e) {
            System.out.println("Ошибка: " + e.getMessage());
        }
    }
}

class Equation {
    private double a;
    private double b;
    private double c;
    private List<Double> roots;

    public Equation(double a, double b, double c) {
        setA(a);
        setB(b);
        setC(c);
        this.roots = new ArrayList<>();
    }

    public double getA() { return a; }
    public double getB() { return b; }
    public double getC() { return c; }
    public List<Double> getRoots() { return new ArrayList<>(roots); }

    public void setA(double a) {
        if (Double.isNaN(a)) throw new IllegalArgumentException("Коэффициент A должен быть числом");
        this.a = a;
    }

    public void setB(double b) {
        if (Double.isNaN(b)) throw new IllegalArgumentException("Коэффициент B должен быть числом");
        this.b = b;
    }

    public void setC(double c) {
        if (Double.isNaN(c)) throw new IllegalArgumentException("Коэффициент C должен быть числом");
        this.c = c;
    }

    private List<Double> solveLinearCase() {
        // A=0, B=0
        if (c == 0) {
            System.out.println("Уравнение превращается в тождество: 0 = 0");
            return Arrays.asList(Double.POSITIVE_INFINITY); // Обозначение для "все действительные числа"
        } else {
            return new ArrayList<>();
        }
    }

    private List<Double> solveQuadraticCase() {
        // A=0, B≠0
        List<Double> roots = new ArrayList<>();
        double xSquared = -c / b;

        if (xSquared > 0) {
            double x1 = Math.sqrt(xSquared);
            double x2 = -x1;
            roots.add(x1);
            roots.add(x2);
        } else if (xSquared == 0) {
            roots.add(0.0);
        }

        return roots;
    }

    private List<Double> solveBiquadraticCase() {
        // A≠0
        List<Double> roots = new ArrayList<>();
        double discriminant = b * b - 4 * a * c;

        if (discriminant < 0) {
            return roots;
        } else if (discriminant == 0) {
            double y = -b / (2 * a);
            if (y > 0) {
                double x1 = Math.sqrt(y);
                double x2 = -x1;
                roots.add(x1);
                roots.add(x2);
            } else if (y == 0) {
                roots.add(0.0);
            }
        } else {
            double sqrtDiscriminant = Math.sqrt(discriminant);
            double y1 = (-b + sqrtDiscriminant) / (2 * a);
            double y2 = (-b - sqrtDiscriminant) / (2 * a);

            for (double y : new double[]{y1, y2}) {
                if (y > 0) {
                    double x1 = Math.sqrt(y);
                    double x2 = -x1;
                    roots.add(x1);
                    roots.add(x2);
                } else if (y == 0) {
                    roots.add(0.0);
                }
            }
        }

        Set<Double> uniqueRoots = new TreeSet<>();
        for (Double root : roots) {
            uniqueRoots.add(root);
        }

        return new ArrayList<>(uniqueRoots);
    }

    public List<Double> solve() {
        roots.clear();

        if (a == 0) {
            if (b == 0) {
                roots = solveLinearCase();
            } else {
                roots = solveQuadraticCase();
            }
        } else {
            roots = solveBiquadraticCase();
        }

        return roots;
    }

    public void displaySolution() {
        System.out.printf("%nУравнение: %.2fx⁴ + %.2fx² + %.2f = 0%n", a, b, c);

        if (a == 0) {
            if (b == 0) {
                System.out.println("Уравнение линейное");
            } else {
                System.out.println("Уравнение квадратное (A = 0)");
            }
        } else {
            double discriminant = b * b - 4 * a * c;
            System.out.printf("Дискриминант: %.4f%n", discriminant);
        }

        if (roots.isEmpty()) {
            System.out.println("Действительных корней нет");
        } else if (roots.size() == 1 && roots.get(0).equals(Double.POSITIVE_INFINITY)) {
            System.out.println("Решение: все действительные числа");
        } else {
            System.out.print("Корни: ");
            List<String> rootStrings = new ArrayList<>();
            for (int i = 0; i < roots.size(); i++) {
                rootStrings.add(String.format("x%d = %.4f", i + 1, roots.get(i)));
            }
            System.out.println(String.join(", ", rootStrings));
        }
    }
}

class InputHandler {
    private Scanner scanner;

    public InputHandler() {
        this.scanner = new Scanner(System.in);
    }

    public boolean isValidDouble(String value) {
        if (value == null) return false;
        try {
            Double.parseDouble(value);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    public double getCoefficient(String prompt, String paramValue) {
        while (true) {
            if (paramValue != null && isValidDouble(paramValue)) {
                double value = Double.parseDouble(paramValue);
                System.out.println(prompt + value);
                return value;
            } else {
                System.out.print(prompt);
                String input = scanner.nextLine().trim().replace(',', '.');
                if (isValidDouble(input)) {
                    return Double.parseDouble(input);
                }
                System.out.println("Ошибка: введите действительное число");
            }
            paramValue = null;
        }
    }
}
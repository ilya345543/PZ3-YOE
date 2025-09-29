# main.py
from ex_2 import op_cube, op_square, op_disk_area, op_sin, op_cos, op_abs
from ex_3 import draw_xy, print_xy_table
from ex_1 import timeit_deco, trace_deco

def frange(a, b, step):
    vals = []
    x = a
    while (step > 0 and x <= b) or (step < 0 and x >= b):
        vals.append(x)
        x += step
    return vals

def choose_func():
    print("Выберите функцию:")
    print("1) op_cube(x)")
    print("2) op_square(x)")
    print("3) op_disk_area(x) — π*r^2")
    print("4) op_sin(x)")
    print("5) op_cos(x)")
    print("6) op_abs(x)")
    choice = input("Ваш выбор: ").strip()
    mapping = {
        "1": (op_cube, "op_cube(x)"),
        "2": (op_square, "op_square(x)"),
        "3": (op_disk_area, "op_disk_area(x)"),
        "4": (op_sin, "op_sin(x)"),
        "5": (op_cos, "op_cos(x)"),
        "6": (op_abs, "op_abs(x)"),
    }
    return mapping.get(choice, (op_cube, "op_cube(x)"))

@timeit_deco
@trace_deco
def compute_y(f, X):
    return [f(x) for x in X]

if __name__ == "__main__":
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))
    step = float(input("Введите шаг: "))
    f, fname = choose_func()

    X = frange(a, b, step)
    Y = compute_y(f, X)

    print(f"\nФункция: {fname}")
    print_xy_table(X, Y, a=min(a, b), b=max(a, b))
    draw_xy(X, Y, a=min(a, b), b=max(a, b), title=fname)

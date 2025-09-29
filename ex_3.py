# ex_3.py
import matplotlib.pyplot as plt

def _slice_range(x, y, a=None, b=None):
    if a is None or b is None:
        return list(x), list(y)
    x2, y2 = [], []
    for xi, yi in zip(x, y):
        if a <= xi <= b:
            x2.append(xi)
            y2.append(yi)
    return x2, y2

def draw_xy(x, y, a=None, b=None, title="График"):
    x2, y2 = _slice_range(x, y, a, b)
    if not x2:
        print("Нет точек для построения графика.")
        return
    plt.figure()
    plt.plot(x2, y2)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(title)
    plt.grid(True)
    plt.show()

def print_xy_table(x, y, digits=3, a=None, b=None):
    x2, y2 = _slice_range(x, y, a, b)
    if not x2:
        print("Нет данных для печати.")
        return
    fmt = f"{{:.{digits}f}}"
    sx = [fmt.format(v) for v in x2]
    sy = [fmt.format(v) for v in y2]
    w = max(max(map(len, sx)), max(map(len, sy)))
    row_x = " ".join(s.rjust(w) for s in sx)
    row_y = " ".join(s.rjust(w) for s in sy)
    print("X:", row_x)
    print("Y:", row_y)

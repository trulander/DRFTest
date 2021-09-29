from math import sqrt


def add(a, b):
    res = a + b
    print(f"{a} + {b} = {res}")
    return res

def square_equation_solver(a, b, c):
    if not all(
        map(
            lambda p: isinstance(p, (int, float)),
            (a, b, c),
        )
    ):
        raise TypeError("Not valid type for param")
    # print("Types are ok")
    if a == 0:
        if b == 0:
            return None, None
        return -c / b, None

    d = b ** 2 - 4 * a * c
    if d < 0:
        return None, None

    d_root = sqrt(d)
    devider = 2 * a
    x1 = (-b + d_root) / devider
    x2 = (-b - d_root) / devider

    if d == 0:
        x2 = None
    elif x2 > x1:
        x1, x2 = x2, x1

    return x1, x2
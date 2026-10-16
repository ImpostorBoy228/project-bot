def f(x: int, y: int) -> int:
    if x > y:
        return 0
    if x == y:
        return 1
    if x == 15:
        return 0
    return f(x + 1, y) + f(x + 2, y)


print(f(3, 9) * f(9, 20))

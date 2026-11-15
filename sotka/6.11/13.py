def f(c,e):
    if c==e:
        return 1
    if c<e:
        return 0
    return f(c-4,e)+f(c//3,e)

print(f(36,2))

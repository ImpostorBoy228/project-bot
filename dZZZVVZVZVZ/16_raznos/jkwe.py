def f(n):
    if n<10:
        return n
    else:
        return n**2 + f(n-15)

print(f(1000)-f(940))

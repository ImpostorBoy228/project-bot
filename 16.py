import sys
sys.setrecursionlimit(490875)
def f(n):
    if n<3:
        return n
    else:
        return (n-1)*f(n-2)
print((f(2024)-f(2022))/f(2020))

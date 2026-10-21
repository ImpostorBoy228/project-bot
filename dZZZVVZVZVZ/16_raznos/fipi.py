import sys
sys.setrecursionlimit(30000)
def f(n):
    if n==1:
        return 2
    return 3*f(n-1)-n

print((f(2025)-f(2023)-1)/(3**2022))

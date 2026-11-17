import sys
sys.set_int_max_str_digits(34535434)
sys.setrecursionlimit(13242134)
def f(n):
    if n==1:
        return 1
    if n>1:
        return n*f(n-1)

print((f(3238)//2 + f(3237))//f(3236))

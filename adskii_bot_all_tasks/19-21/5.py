import functools

def moves(n):
    return n+1,n+4,n*3

@functools.lru_cache(None)
def g(s,x):
    if s>=67: return False
    if x==0: return False
    for i in moves(s):
        if i>=67: return True
        if not g(i,x-1): return True
    return False

for s in range(1, 67):
    if g(s, 1):
        print(s)

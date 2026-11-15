def sm(n):
    s=""
    while n>0:
        s=str(n%7) + s
        n//=7
    return s

print(sm(5**2 * 7**25 + 6**2 * 7**36 - 4**2 * 9**3).count("0"))
print(sm(5**2 * 7**25 + 6**2 * 7**36 - 4**2 * 9**3))

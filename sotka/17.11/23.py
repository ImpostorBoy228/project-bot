def f(x,y):
    if x>y:
        return 0
    if x==y:
        return 1
    re = str(x)
    fi=re[-2]
    l=re[-1]
    re = re[:-2] + l+fi

    if fi>=l:
        return f(x+1,y)
    return f(x+1,y)+f(int(re),y)


print(f(100,150))

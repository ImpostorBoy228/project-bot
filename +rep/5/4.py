def f(n):
    s = bin(n)[2:]
    return int(s + s[-2] + s[1], 2)

def main():
    hu = 99999
    for i in range(2,999):
        o = f(i)
        if o > 150:
            hu = min(hu,i)

    print(hu)


if __name__ == "__main__":
    main()

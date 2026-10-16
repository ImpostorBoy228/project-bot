for n in range(2131):
    size = 126 + 60*8 + len(bin(n)[2:])
    size *= n
    if size > 80*1024*8:
        print(n-1)
        break

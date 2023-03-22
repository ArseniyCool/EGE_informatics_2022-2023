for n in range(1, 10000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = r + '00'
    else:
        r = r + '10'
    if int(r, 2) > 452:
        print(int(r, 2))
        break
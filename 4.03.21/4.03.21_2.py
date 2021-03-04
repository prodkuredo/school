with open('1_A.txt', 'r') as f:
    t = str(f.read())
    smax = 1
    s = 1
    for i in range(1, len(t)):
        if (t[i] != t[i-1]):
            s += 1
            if s >= smax:
                smax = s
        else:
            s = 1
    print(smax)
for i in range(1204300, 1204380+1):
    d = []
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            d.append(j)
            d.append(i//j)
    d = [j for j in d if j%2==0]
    s = sum(d) if len(d) > 0 else 0
    if s != 0 and s % 10==0:
        print(i, s)

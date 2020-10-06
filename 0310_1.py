a = [1, 2, 3, 'asd']
b = [1, 2, 4, 3, 'qweqw', 123]
def asd(a,b):
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                c.append(a[i])
    print(c)
asd(a, b)



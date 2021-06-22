for i in range(1, 10000):
    s = ''
    x = i
    a = 125**200 - 5**x + 74
    while a > 0:
        s = s + str(a%5)
        a //= 5
    if s.count('4') == 100:
        print(i)
        break

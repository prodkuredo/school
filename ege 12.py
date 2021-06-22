for a1 in range(1, 100):
    for a2 in range(1, 100):
        s = '0'+'1'*a1 + '2'*a2
        while '02' in s or '01' in s:
            s = s.replace('01', '2202')
            s = s.replace('02', '10')
        if s.count('1') == 40 and s.count('2') == 64:
            print(a2)

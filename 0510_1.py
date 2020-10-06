l = {'A':0, 'B': 1101, 'C' :101, 'D':1100, 'E': 100, 'F': 111}
x = str(input('Введите сообщение '))
y = []
if x.isalpha():
    print('закодировать')
    for i in x: 
        y.append(l[i])
    print(''.join([str(q) for q in y]))
else:
    print('декодировать')
    l1 = dict([(m, n) for n, m in l.items()])
    #ya ukral sleduyushie stroki u artema :c
    b = list(map(int, x.strip().split()))
    for num in b:
        y.append(l1[num])
    print(''.join(y))
    #ya zamotalsya, eshe delat` geometriyu :,c
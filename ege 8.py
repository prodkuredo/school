a = ['м', 'а', 'т', 'в', 'е', 'й']
count = 0
g = list(itertools.permutations(a,r=6)
                 #.product(a, repeat=6), если не нужно, чтобы буквы повторялись только один раз
for i in g:
    if ''.join(i)[0] != 'й' and ''.join(i).count('ае') == 0:
        count += 1
print(count)

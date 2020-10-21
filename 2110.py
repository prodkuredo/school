with open('out.txt', 'w') as f:
    for i in range(1, 11):
        for j in range(i, i*11, i):
            f.write(str(str(j) + '\t'))
        f.write('\n')
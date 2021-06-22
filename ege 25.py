with open('24.txt', 'r') as f:
    s = f.readline()
    a = 1
    maxim = 0
    for i in range(len(s)-1):
        if  s[i] in '123' and s[i+1] in '123' and s[i] <= s[i+1]:
            a += 1
            maxim = max(maxim, a)
        else:
            a = 1
print(maxim)

import random
n = 1000
a = []
b = []
for i in range(n):
    a.append(random.randint(0, 50))
print(a)
for i in range(len(a)): 
    if a[i] != 20:
        b.append(a[i])
print(b, a.count(20), 'Вхождений числа 20')
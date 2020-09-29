import random
n = 500
l = []
k = []
for i in range(n):
    l.append(random.randint(0, 100))
print(l)
for i in range(n):
    if l[i] < 20 or l[i] > 25:
        k.append(l[i])
print(k)
for i in range(len(k)):
    k[i] = k[i]**2
print(k)

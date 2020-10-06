import random
n = 20
a = []
for i in range(n):
    a.append(random.randint(1, 10))
print(a)
for i in range(n):
    l = i
    for j in range(i, n):
        if a[j] > a[l]:
            l = j
    a[i], a[l] = a[l], a[i]
def qwerty(a):
    for i in range(len(a)):
        k = a.count(a[i])
        if k > 1:
            if a[i] != a[i-1]:
                print(a[i], ':', k, 'раз')
qwerty(a)
print()

                

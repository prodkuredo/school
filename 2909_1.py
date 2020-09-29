import random
n = 300
list1 = []
for i in range(n):
    list1.append(random.randint(0, 100))
print(list1)
for i in range(n):
    l = i
    for j in range(i, n):
        if list1[j] > list1[l]:
            l = j
    list1[i], list1[l] = list1[l], list1[i]
print(list1)
print(list(reversed(list1)))
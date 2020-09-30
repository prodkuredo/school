import math
def q(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        return ((-b + math.sqrt(d))/(2*a)), ((-b - math.sqrt(d))/(2*a))
    elif d == 0:
        return (-b/(2*a))
    else:
        return ('нет корня')
print(q (1,2,-3))
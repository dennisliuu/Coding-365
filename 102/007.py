import math


def y(choosef, a, x):
    if choosef == 1:
        y = math.sqrt(a - x * x)
    elif choosef == 2:
        y = (a * x * x * x + 7 * x) / math.sqrt(a + x)
    return y


def f(choosef, a, p, q, err):
    n = 1
    h = 0
    total = 0
    last = 0
    while 1:
        h = (q - p) / n
        total = 0
        for i in range(n):
            total += (y(choosef, a, p + i * h) + y(choosef, a, p + (i + 1) * h)) * h / 2
        if abs(total - last) < 1 / 10**err:
            break
        last = total
        n+=1
    print(int(total*100000)/100000)


input_String = input().split(',')
choosef = int(input_String[0])
a = int(input_String[1])
p = int(input_String[2])
q = int(input_String[3])
err = int(input_String[4])
f(choosef,a,p,q,err)


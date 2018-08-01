import math
x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
x6 = int(input())
p1 = (x1, x2)
p2 = (x3, x4)
p3 = (x5, x6)
total = 0
if p2[0] >= p1[0] and p2[0] <= p1[1]:
    # total = x4-x1
    if p3[0] >= p1[0] and p3[0] <= p2[1]:
        print(abs(x6-x1))
    else:
        print(abs(x4 - x1) + abs(x6 - x5))
else:
    # x2-x1
    if p3[0] >= p2[0] and p3[0] <= p2[1]:
        print(abs(x6 - x3) + abs(x2 - x1))
    else:
        print(abs(x2-x1)+abs(x4-x3)+abs(x6-x5))
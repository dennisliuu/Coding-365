import math
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
T = b*b-4*a*c
if T < 0:
    print("r1=%.1f+%.1fi\nr2=%.1f-%.1fi" %(
    (-1 * b)/(2*a),
    (math.sqrt(math.fabs(T)))/(2*a),
    (-1 * b)/(2*a),
    (math.sqrt(math.fabs(T)))/(2*a)))
else:
    x1 = ((-1 * b) + math.sqrt(T))/(2*a)
    x2 = ((-1 * b) - math.sqrt(T))/(2*a)
    print(x1)
    print(x2)

import math
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
x1 = ((-1 * b) + math.sqrt(b*b-4*a*c))/(2*a)
x2 = ((-1 * b) - math.sqrt(b*b-4*a*c))/(2*a)
print(x1)
print(x2)
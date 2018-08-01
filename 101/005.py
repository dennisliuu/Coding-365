import math
a = round(float(input()), 2)
b = round(float(input()), 2)
c = round(float(input()), 2)
d = round(float(input()), 2)
e = round(float(input()), 2)
total = a + b + c + d + e
aver = total / 5.0
print('%.2f' % aver)
diff = (math.pow(a - aver,2) + math.pow(b - aver,2) + math.pow(c - aver,2) + math.pow(d - aver,2) + math.pow(e - aver,2)) / 5
print('%.2f' % diff)
print('%.2f' % math.sqrt(diff))

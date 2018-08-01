a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))

def compute(a, b, c):
    if a + b <= c or a + c <= b or c + b <= a:
        return 0
    elif a*a + b*b == c*c or a*a + c*c == b*b or c*c + b*b == a*a:
        return 1
    elif a*a + b*b < c*c or a*a + c*c < b*b or c*c + b*b < a*a:
        return 2
    elif a*a + b*b > c*c or a*a + c*c > b*b or c*c + b*b > a*a:
        return 3
    else:
        return 0
if compute(a, b, c) is 0:
    print('Not Triangle')
elif compute(a, b, c) is 1:
    print('Right Triangle')
elif compute(a, b, c) is 2:
    print('Obtuse Triangle')
elif compute(a, b, c) is 3:
    print('Acute Triangle')
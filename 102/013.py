def mm(m, n):
    """求两个整数的最小公倍数"""
    if m > n:
        m, n = n, m
    if m == n or m == 1 or n % m == 0:
        return n
    for i in range(2, n+1):
        if m * i % n == 0:
            return m * i
 
         
def mn(m, n):
    """求两个整数的最小公约数"""
    if m > n:
        m, n = n, m
    if m == n or m == 1 or n % m == 0:
        return m
    r = 1
    for i in range(2, m):
        if m % i == 0 and n % i  == 0:
            r = i
    return r
 
 
def show(a):
    """[1, 1, 2] --> '1 1/2'"""
    if a[0] == 0:
        return '{}/{}'.format(a[1], a[2])
    else:
        return '{}({}/{})'.format(*a)
 
 
def imp(a):
    """1 1/2 --> 3/2"""
    if a[0] == 0:
        return [a[0]*a[2]+a[1], a[2]]
    else:
        return [a[0]*a[2]+(a[0]//abs(a[0]))*a[1], a[2]]
 
 
def unimp(a):
    """3/2 --> 1 1/2"""
    m = mn(abs(a[0]), a[1])
    n, d = a[0] // m, a[1] // m
    if n < d:
        return 0, n, d
    else:
        return (n//abs(n))*(abs(n) // d), abs(n) % d, d 
 
 
def add(a, b):
    a, b = imp(a), imp(b)
    m = mm(a[1], b[1])
    r = a[0] * m // a[1] + b[0] * m // b[1], m
    return unimp(r)

def mul(a, b):
    a, b = imp(a), imp(b)
    r = a[0] * b[0] , a[1] * b[1]
    return unimp(r)

Str_input = input().split('/')
a = [0]
for i in Str_input:
    a.extend(i)
a = list(map(int, a))
print(a)

Str_input = input().split('/')
b = [0]
for i in Str_input:
    b.extend(i)
b = list(map(int, b))
print(b)

if a[1] == 0 or b[1] == 0:
    print('ERROR')
else:
    add_result = show(add(a, b))
    mul_result = show(mul(a, b))
    print(add_result)
    print(mul_result)
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
    return '{} {}/{}'.format(*a)
 
 
def imp(a):
    """1 1/2 --> 3/2"""
    return [a[0]*a[2]+(a[0]//abs(a[0]))*a[1], a[2]]
 
 
def unimp(a):
    """3/2 --> 1 1/2"""
    m = mn(abs(a[0]), a[1])
    n, d = a[0] // m, a[1] // m
    return (n//abs(n))*(abs(n) // d), abs(n) % d, d 
 
 
def add(a, b, negative=False):
    a, b = imp(a), imp(b)
    m = mm(a[1], b[1])
    sign = -1 if negative else 1
    r = a[0] * m // a[1] + sign * b[0] * m // b[1], m
    return unimp(r)
 
def main():
    a = [-7, 3, 4]
    b = [3, 8, 3]
    s = '+'
    result = show(add(a, b, s=='-'))
    print(result)
 
if __name__ == '__main__':
    main()
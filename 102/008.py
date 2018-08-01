def Fibonacci(x):
    a = 1
    b = 1
    c = 0
    i = 3
    if x==1 or x==2:
        return(a)
    else:
        while i < x + 1:
            c = a + b
            a = b
            b = c
            i += 1
    return(c)

lst_x = []
while 1:    
    x = int(input())
    lst_x.append(x)
    if x == -1:
        for i in lst_x[::-1]:
            print(Fibonacci(i))
        break
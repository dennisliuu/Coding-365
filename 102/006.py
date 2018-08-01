selectFunction = int(input())
n = int(input())
c = int(input())
d = int(input())
err = int(input())


def f1(x, n, c, d):
    return x**n - c*x**(n-2) - d


def f1_derivative(x, n, c, d):
    return n*x**(n-1)-(c*(n-2))*x**(n-3)


x = [0] * 100
stop_point = 1
if selectFunction == 1:
    x[0] = d / 2
    for j in range(1, len(x) + 1):
        x[j] = x[j-1] - f1(x[j-1], n, c, d) / f1_derivative(x[j-1], n, c, d)
        if x[j-1] - x[j] < 1 / 10**err:
            stop_point = j
            break


print(int(x[stop_point]*10**(err+1))/10**(err+1))

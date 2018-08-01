x = input()


def find_Prime(k):
    k = int(k)
    lst_Prime = []
    for p in range(2, k + 1):
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            lst_Prime.append(p)
    print(max(lst_Prime))


def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def is_float_post(n):
    try:
        float(n)
        if float(n) > 0:
            return True
    except ValueError:
        return False


def is_float_nati(n):
    try:
        float(n)
        if float(n) < 0:
            return True
    except ValueError:
        return False


if x == '0' or x == '1':
    find_Prime(1000)
elif x.isdigit():
    find_Prime(x)
elif is_digit(x):
    find_Prime(int(x) * - 1 * 11)
elif is_float_post(x):
    find_Prime(x.split('.')[0])
elif is_float_nati(x):
    find_Prime(x.split('.')[1])
else:
    print('error')

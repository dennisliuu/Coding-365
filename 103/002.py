data = [int(x) for x in input().split()]
temp = [i // 10 for i in data]
sz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4]


def judge(data):
    if data[0] % 10 == data[1] % 10 == data[2] % 10 == data[3] % 10 == data[4] % 10:
        print(7 if ''.join(map(str, sorted(temp)))
              in ''.join(map(str, sz)) else 0)
    else:
        from itertools import groupby
        cond = [len(list(group)) for key, group in groupby(sorted(temp))]
        if ''.join(map(str, sorted(temp))) in ''.join(map(str, sz)):
            print(6)
        elif cond == [1, 1, 1, 2]:
            print(1)
        elif cond == [2, 2, 1]:
            print(2)
        elif cond == [3, 1, 1]:
            print(3)
        elif cond == [3, 2]:
            print(4)
        elif cond == [4, 1]:
            print(5)
        else:
            print(0)


judge(data)

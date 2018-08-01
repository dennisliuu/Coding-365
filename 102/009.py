input_String = input().split(' ')
# print(input_String)

bottle_need = input_String[0]
bottle_own = input_String[1]
poki_num = input_String[2]


def process(bottle_need, bottle_own, poki_num):
    original_poki = poki_num
    for i in range(1, poki_num + 1):
        # print(bottle_need, bottle_own, poki_num)
        if bottle_own + bottle_need >= 0:
            bottle_own += bottle_need
            bottle_own += 1.5
            poki_num -= 1
            bottle_own += 1.5
        else:
            return original_poki - poki_num


if len(bottle_need.rsplit('.')[-1]) == 1 and float(bottle_need) < 0 and len(bottle_own.rsplit('.')[-1]) == 1 and float(bottle_own) >= 0 and poki_num.isdigit():
    print(process(float(bottle_need), float(bottle_own), int(poki_num)))
else:
    print('Error')

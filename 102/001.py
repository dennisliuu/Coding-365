def test_func(num_list):
    start = 9999
    end = -9999
    for one_list in num_list:
        if one_list[0] < start:
            start = one_list[0]
        if one_list[1] > end:
            end = one_list[1]
    print(start, end)
    flag = ['false'] * end
    for i in range(len(num_list)):
        for j in range(num_list[i][0], num_list[i][1]):
            flag[j] = True
            # print flag
    return flag.count(True)


n = int(input("n: "))
l = []

for i in range(n):
    row_list = []
    for j in range(2):
        row_list.append(int(input())+1000)
    l.append(row_list)

print(l)
print('Total Length is:', test_func(l))

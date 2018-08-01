# N = int(input())
# lst = [[0 for j in range(N)] for i in range(N)]
# for i in range(N):
#     lst[i] = input().split(' ')
# print(lst)
lst = [['0', '4', '2', '3', '6'], ['4', '0', '3', '1', '4'], ['2', '3', '0', '2', '5'], ['3', '1', '2', '0', '3'], ['6', '4', '5', '3', '0']]
nextone = 0
for i in range(5):
    nextone = int(min(filter(lambda j: int(j) > 0, lst[nextone])))
    print(nextone)
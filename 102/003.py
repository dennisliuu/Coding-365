import math

triType = input()
triHeight = int(input())

if triType == '1':
    for i in range(1, (triHeight + 1) // 2 + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()
    for i in range(1, (triHeight + 1) // 2):
        for j in range(1, (triHeight + 1) // 2 - i + 1):
            print(j, end='')
        print()
elif triType == '2':
    for i in range(1, (triHeight + 1) // 2 + 1):
        for j in range(1, (triHeight + 1) // 2 - i + 1):
            print('.', end='')
        for j in range(i, 0, -1):
            print(j, end='')
        print()
    for i in range(1, (triHeight + 1) // 2):
        for j in range(0, i):
            print('.', end='')
        for j in range((triHeight + 1) // 2 - i, 0, -1):
            print(j,end='')
        print()

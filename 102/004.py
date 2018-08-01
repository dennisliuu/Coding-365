import math

height = int(input())
# height = 7
for i in range(1, height // 2 + 2):
    for j in range((height // 2 + 1) - i):
        print('.', end='')
    for j in range(0, i * 2 - 1):
        print('*', end='')
    for j in range((height // 2 + 1) - i):
        print('.', end='')
    print()
for i in range(1, height // 2 + 1):
    for j in range(0, i):
        print('.', end='')
    for j in range(0, height - 2 * i):
        print('*', end='')
    for j in range(0, i):
        print('.', end='')
    print()
temp = 99
total = 0
i = 0
while i < 4:
    i+=1
    temp = int(input())
    if temp == 10:
        i-=1
    total += temp
print(total)
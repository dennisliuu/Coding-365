scores = []
total = 0
for i in range(21):
    scores.append(int(input()))

l = [scores[i:i + 2] for i in range(0, 18, 2)]
l.append(scores[-3:])
print(l)
for i in range(len(l[:-1])):
    if l[i][0] == 10:
        try:
            total += 10 + sum(l[i + 1])
        except IndexError:
            total += 10
    elif sum(l[i]) == 10:
        try:
            total += 10 + l[i + 1][0]
        except IndexError:
            total += 10
    else:
        total += sum(l[i])
    print(total)
print(total + sum(l[-1]))

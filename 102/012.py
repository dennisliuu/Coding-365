def compute(x1, y1, x2, y2):
    a = abs(x1 - x2)
    b = abs(y1 - y2)
    return a*b, (a + b) * 2

lst_area = []
lst_perimeter = []

while 1:
    x1 = int(input())
    if x1 == -1:
        break
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    area, perimeter = compute(x1, y1, x2, y2)
    lst_area.append(area)
    lst_perimeter.append(perimeter)

print(max(lst_area), max(lst_perimeter))
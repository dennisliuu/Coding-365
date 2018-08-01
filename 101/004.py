a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

def getTriangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a + b < c or a + c < b or c + b < a:
        return 1
    else:
        if a == b == c:
            return 2
        if a == b or c == b or a == c:
            return 3
    return 4
print(getTriangle(a, b, c))

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

base = input()
numBase10 = input()

base = int(base)
numBase10 = int(numBase10)
if 2 <= base <= 9 and 0 <= numBase10 <= 10000000:
	print(baseN(numBase10, base))
else:
	print(-1)

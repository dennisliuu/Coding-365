ans = []

class university(object):
	def __init__(self, name, props):
		self.name = name
		self.props = props

unis = []

n = int(input())
if n > 10:
	exit()

for i in range(n):
	inp = input()
	inp = inp.split(' ')
	unis.append(university(inp[0], inp[1:]))

m = int(input())
if m > 10:
	exit()

for i in range(m):
	inp = input().replace(" ", "").split('+')
	for j in inp:
		for k in unis:
			if len(j) == 2 and j in k.props:#AABB
				ans.append(k.name)
			else:
				sub_prop = [j[l:l+2] for l in range(0,len(j),2)] #sub_prop=[AA,BB]
				if set(sub_prop).issubset(k.props): #set1<=set2 return true
					ans.append(k.name)
	ans.append('\n')

final_ans = []
for i in ans:
	if i != '\n':
		final_ans.append(i)
	else:
		final_ans = sorted(list(set(final_ans)))
		print(*final_ans)
		final_ans = []#clear \n 前ans


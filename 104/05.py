# Class for university
# Class has name prop(list)
# Input remove space
# Class compare function
# Sorted user list vs sorted uni list

class university(object):
	def __init__(self, name, props):
		self.name = name
		self.props = props

# a = university('aaaa', ['1','2'])
# print(a.name)
unis = []
n = int(input())
ans = []
unis_names = []

for i in range(n):
	inp = input()
	unis.append(university(inp.split(' ')[0], inp.split(' ')[1:]))

for i in unis:
	# print(i.name, i.props)
	unis_names.append(i.name)

m = int(input())
for i in range(m):
	inp = input().replace(" ","").split('+')
	# print(inp)
	for i in inp:
		for j in unis:
			if len(i) > 2:
				sub_prop = [i[k:k+2] for k in range(0, len(i), 2)]
				if set(sub_prop).issubset(j.props):
					ans.append(j.name)
			if i in j.props:
		 	 	ans.append(j.name)
	ans.append('\n')

# print(unis_names)
# print(ans)

for i in ans:
	if i != '\n':
		print(i, end=" ")
	else:
		print(i, end="")

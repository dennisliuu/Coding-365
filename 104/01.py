class bankAccount(object):
	def __init__(self, name, balance=0.00):
		self.name = name
		self.balance = balance
	def deposit(self, amount):
		self.balance += amount
	def withdraw(self, amount):
		self.balance -= amount
	def balance(self):
		return self.balance

def showPersentage(b1, b2):
	if b1 <= 0 and b2 > 0:
		return 'A:0%,B:100%'
	elif b1 > 0 and b2 <= 0:
		return 'A:100%,B:0%'
	elif b1 == 0 and b2 == 0:
		return 'A:50%,B:50%'
	perA = int(b1/(b1 + b2)*10000//100)
	perB = 100 - perA
	ans = 'A:{}%,B:{}%'.format(perA, perB)
	return ans

customerA = bankAccount('a')
customerB = bankAccount('b')
inp = 'n'
answer = []

while 1:
	if inp == 'n':
		inp = input()
	if inp == 'e':
		break

	# print('Select %s' % inp.upper())
	answer.append('Select %s' % inp.upper())

	while 1:

		steps = input()

		if steps == 'v':
			# print('%s:%d' % (inp.upper(), customerA.balance if inp == 'a' else customerB.balance))
			answer.append('%s:%d' % (inp.upper(), customerA.balance if inp == 'a' else customerB.balance))
		if steps == 's':
			numbers = int(input())
			customerA.deposit(numbers) if inp == 'a' else customerB.deposit(numbers)
			# if inp == 'a':
			# 	customerA.deposit(numbers)
			# else:
			# 	customerB.deposit(numbers)
			# print('%s:Deposit,%d' % (inp.upper(), numbers))
			answer.append('%s:Deposit,%d' % (inp.upper(), customerA.balance if inp == 'a' else customerB.balance))

		if steps == 'w':
			numbers = int(input())
			customerA.withdraw(numbers) if inp == 'a' else customerB.withdraw(numbers)
			# if inp == 'a':
			# 	customerA.withdraw(numbers)
			# else:
			# 	customerB.withdraw(numbers)
			# print('%s:Withdraw,%d' % (inp.upper(), numbers))
			answer.append('%s:Withdraw,%d' % (inp.upper(), customerA.balance if inp == 'a' else customerB.balance))

		if steps == 'p':
			# print(showPersentage(customerA.balance, customerB.balance))
			answer.append(showPersentage(customerA.balance, customerB.balance))

		if steps == 'a' or steps == 'b' or steps == 'e':
			inp = steps
			break

for i in answer:
	print(i)

# print(repr(customer1))
# customer1.deposit(100)
# customer1.withdraw(30)
# print(customer1.balance)
# customer2 = bankAccount('Sam', 200)
# print(showPersentage(customer1.balance, customer2.balance))

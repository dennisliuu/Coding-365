def intro():
	print("猜數字遊戲	    				   	    	 ")
	print()
	print("遊戲規則：")
	print("1.每回合電腦會猜一個四位數字                 ")
	print("2.A的次數代表電腦猜對了幾個數字且位置正確    ")
	print("3.B的次數代表電腦猜對了幾個數字但位置不對    ")
	print("4.必須告訴電腦A和B的值                       ")
	    
def think():
	num = [0]*4
	isOver = 0
	a = 0
	b = 0
	answerBase = ["%d" % i for i in range(1,10000)]
	a = []
	list = str([0,1,2,3,4,5,6,7,8,9])
	n = 0
	for i in answerBase:
	    for j in list:
	        if i.count(j) == 0:
	        	a.append(i)
	print(answerBase)
	remain = 5040

	inp = input()
	ans = int(inp.split(',')[0])
	a = int(inp.split(',')[1].split('a')[0])
	# a_s = inp.split('')[3]
	b = int(inp.split('a')[1].split('b')[0])
	# bs = inp.split('')[5]

	refer = num

	for i in range(0, remain):
		#填裝a值和b值，但要區別於之前的人類輸入的a值b值 
		aa = 0
		bb = 0
		#以下兩個for用來比對第i個答案和亂數取的答案的是幾a幾b 
		for j in range(0, 4):
			for k in range(0, 4):
				if answerBase[i][j] == refer[k]:
					if j == k:
						aa+=1
					else:
						bb+=1
		#把a值b值相等的答案保留下來 
		if not((aa==a) and (bb==b)):
			for j in range(i, remain):  
				for k in range(0, 4):
					answerBase[j][k] = answerBase[j+1][k]
			remain-=1
			i-=1
	if remain==1:
		print()
		print("答案是")
		for i in range(0, 4):
			print("%d" % answerBase[randNum][i],"")
		isOver=1
    #發現沒有答案符合玩家想的數字，就是玩家作弊！
	if remain==0:  
		print()
		print("E04沒答案啦")
		isOver=1

def main():
    intro()
    think()

if __name__ == "__main__":
    main()

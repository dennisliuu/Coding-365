# prepare
isOver = False
answerBase = ['{0:04}'.format(i) for i in range(1,10000)]
list = str([0,1,2,3,4,5,6,7,8,9])
all_ans = []
n = 0

#刪除4位數帶有重複的數字
for i in answerBase:
    for j in list:
        if i.count(j) > 1:
            n += 1
    if n == 0:
        all_ans.append(i)
    n=0
    
last_element = []

def thinka(ans,i,aa):
    ans = str(ans)
    aa = 0
    for j in range(4):
        if  ans[j] == i[j]:
            aa+=1
    return aa
def thinkb(ans,i,bb):
    ans = str(ans)
    bb = 0
    for j in range(4):
        for k in range(4):
            if j != k:
                if ans[j] == i[k]:
                    bb+=1 
    return bb   
def thinkall(last_element, ans, a, b):
    # print(ans, a, b, len(last_element))
    ans = str(ans)
    remain = last_element.copy()
    temp = []
    for i in remain:
        aa = 0
        bb = 0
        aa = thinka(ans,i,aa)
        bb = thinkb(ans,i,bb)
        
        if aa == a and bb == b:
            temp.append(i)

    return temp

count = 1    #計數用

while not isOver:

    inpu = input()
    ans = inpu.split(',')[0]
    a = int(inpu.split(',')[1].split('A')[0])
    b = int(inpu.split('A')[1].split('B')[0])
    
    if last_element == []:
        last_element = thinkall(all_ans, ans, a, b)
        
    else:
        last_element = thinkall(last_element, ans, a, b)
    count += 1       
    # print(last_element)
    if len(last_element) == 1:
        print(last_element[0])
        break
    elif len(last_element) == 0:
        print('no answer')
        break
    
    #當初入超過10次跳出迴圈
    if count >10:
        break
    

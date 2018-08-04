# prepare
isOver = False
answerBase = ['{0:04}'.format(i) for i in range(1,10000)]
list = str([0,1,2,3,4,5,6,7,8,9])
all_ans = []
n = 0
for i in answerBase:
    for j in list:
        if i.count(j) > 1:
            n += 1
    if n == 0:
        all_ans.append(i)
    n=0
# print(len(a))
last_element = []

def think(last_element, ans, a, b):
    # print(ans, a, b, len(last_element))
    ans = str(ans)
    remain = last_element.copy()
    temp = []
    # while len(remain) > 1:
    for i in remain:
        aa = 0
        bb = 0
        for j in range(4):
            if  ans[j] == i[j]:
                aa+=1
        for j in range(4):
            for k in range(4):
                if j != k:
                    if ans[j] == i[k]:
                        bb+=1
        if aa == a and bb == b:
            temp.append(i)
            # print(i)
    return temp

while not isOver:
    inp = input()
    ans = int(inp.split(',')[0])
    a = int(inp.split(',')[1].split('A')[0])
    b = int(inp.split('A')[1].split('B')[0])
    
    if last_element == []:
        last_element = think(all_ans, ans, a, b)
        # print(last_element)
    else:
        last_element = think(last_element, ans, a, b)
        # print(last_element)
    
    if len(last_element) == 1:
        print(last_element[0])
        break
    elif len(last_element) == 0:
        print('no answer')
        break

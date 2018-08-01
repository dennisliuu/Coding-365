def dataInput():
    num = int(input())
    hr = int(input())
    if hr == 1:
        t1 = int(input())
        t2 = "n"
    elif hr == 2:
        t1 = int(input())
        t2 = int(input())
    else:
        check_num = 0
        t1 = int(input())
        t2 = "n"
    return num,hr,t1,t2
    
class1_t2="n"
class2_t2="n"
class3_t2="n"
check_clear=0
check_num=1
class1_num,class1_hr,class1_t1 , class1_t2 = dataInput()
class2_num,class2_hr,class2_t1 , class2_t2 = dataInput()
class3_num,class3_hr,class3_t1 , class3_t2 = dataInput()
    
if check_num == 0 or class1_num > 9999 or class1_num < 1000 or class2_num > 9999 or class2_num < 1000 or class3_num > 9999 or class3_num < 1000:
    print(-1)
    import sys
    sys.exit()

if(class1_t1==class2_t1):
    check_clear=1
    print(class1_num,',',class2_num,',',class1_t1,sep='')
if(class1_t1==class2_t2):
    check_clear=1
    print(class1_num,',',class2_num,',',class1_t1,sep='')
if(class1_t1==class3_t1):
    check_clear=1
    print(class1_num,',',class3_num,',',class1_t1,sep='')
if(class1_t1==class3_t2):
    check_clear=1
    print(class1_num,',',class3_num,',',class1_t1,sep='')
if(class1_t2==class2_t1):
    check_clear=1
    print(class1_num,',',class2_num,',',class1_t2,sep='')
if(class1_t2==class2_t2 and class1_t2 != "n"):
    check_clear=1
    print(class1_num,',',class2_num,',',class1_t2,sep='')
if(class1_t2==class3_t1):
    check_clear=1
    print(class1_num,',',class3_num,',',class1_t2,sep='')
if(class1_t2==class3_t2 and class1_t2 != "n"):
    check_clear=1
    print(class1_num,',',class3_num,',',class1_t2,sep='')

if(class2_t1==class3_t1):
    check_clear=1
    print(class2_num,',',class3_num,',',class2_t1,sep='')
if(class2_t1==class3_t2):
    check_clear=1
    print(class2_num,',',class3_num,',',class2_t1,sep='')
if(class2_t2==class3_t1):
    check_clear=1
    print(class2_num,',',class3_num,',',class2_t2,sep='')
if(class2_t2==class3_t2 and class2_t2 != "n"):
    check_clear=1
    print(class2_num,',',class3_num,',',class2_t2,sep='')
    
if(check_clear==0):
    print('correct')
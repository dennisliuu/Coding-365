# class poly:
#     __a = [0]*20 #存放第一个输入的多项式和运算结果
#     __b = [0]*20#存放输入的多项式
#     __result = [0]*20#结果

#     def __Input(self,f):
#         n = input('依序输入二项式的系数和指数（指数小于10）：').split()
#         for i in range(int(len(n)/2)):
#             f[ int(n[2*i+1])] = int(n[2*i])
#         print(f, n)
#         self.__output(f)

#     def __add(self,a,b):  #加法函数
#         return [a[i]+b[i] for i in range(20)]

#     def __minus(self,a,b):  #减法函数
#             return [a[i]-b[i] for i in range(20)]

#     def __mul(self,a,b):
#         self.__result = [0]*20
#         for i in range(10):#第一个循环：b分别于a[0]到a[9]相乘
#             for j in range(10):  #第二个循环：b[j]*a[i]
#                 self.__result[i+j] = int(self.__result[i+j]) + int(a[i]*b[j])
#         return self.__result

#     def __output(self,a):#输出多项式
#           b = ''
#           for i in range(20):
#             if a[i]> 0:
#                 b = b+'+'+str(a[i])+'X^'+str(i)
#             if a[i]<0:
#                 b = b+"-"+str(-a[i])+'X^'+str(i)
#           print(b[1::])

#     def control(self):
#         print ("二项式运算：\n")
#         self.__Input(self.__a)
#         while True:
#             operator = input('请输入运算符（结束运算请输入‘#’）')#self.Input(self.a)
#             if operator =='#':
#                 return 0
#             else:
#                 self.__b = [0]*20
#                 self.__Input(self.__b)
#                 self.__a = {'+':self.__add(self.__a,self.__b),'-':self.__minus(self.__a,self.__b),'*':self.__mul(self.__a,self.__b)}.get(operator)
#                 print ('计算结果：',end='')
#                 self.__output(self.__a)


# POLY = poly()    #初始化类
# POLY.control()   #通过选取操作符选择相应的运算
# import numpy as np

# # sym = input()

# # 4x^3 - 2x + 3
list1 = []
p1 = input().split(' ')
for i in p1:
    list1.append(i)
print(list1)
t = len(list1)
for i in range(len(list1)):
    if i == t:
        break
    if list1[i] == '-':
        list1[i:i+2] = [''.join(list1[i:i+2])]
        t -= 1
print(list1)
x_times = [s for s in list1 if "x" in s]
print(x_times)
print(
    list(set(list1) - set(x_times)).remove('+')
)
coef = []
for i in range(len(x_times)):
    coef.append(x_times[i].split('x')[0])
    coef.append((x_times[i].split('x')[1]))
for i in range(len(coef)):
    if coef[i] == '':
        coef[i] = 1
    elif coef[i] == '-':
        coef[i] = -1
print(coef)
# # p1 = np.poly1d([4, 0, -2, 3])
# # p2 = np.poly1d([-2, 0, -1, 3, -1, -1])

# # if sym == '+':
# #     print(p1 + p2)
# # elif sym == '-':
# #     print(p1 - p2)
# # elif sym == '*':
# #     print(p1 * p2)

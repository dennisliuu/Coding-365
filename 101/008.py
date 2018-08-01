import numpy as np
num_array = list()
for i in range(5):
    n = int(input("num :"))
    num_array.append(int(n))
print(num_array)
a_183 = [0.08, 0.139, 0.135, 1.128, 1.483]
a_383 = [0.07, 0.130, 0.121, 1.128, 1.483]
a_983 = [0.06, 0.108, 0.101, 1.128, 1.483]
total_183 = round(np.dot(num_array, a_183))
total_383 = round(np.dot(num_array, a_383))
total_983 = round(np.dot(num_array, a_983))

if total_183 < 183:
    print(183, 183)
elif total_183 > 183 and total_183 < 383:
    print(183 ,total_183)
elif total_383 < 383:
    print(383 ,383)
elif total_383 > 383 and total_383 < 983:
    print(383 ,total_383)
elif total_983 < 983:
    print(983 , 983)
else: 
    print(983 , 983)
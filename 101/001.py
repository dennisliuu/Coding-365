name = input("姓名：")
std_id = input("學號：")
score1 = int(input("第一科成績："))
score2 = int(input("第二科成績："))
score3 = int(input("第三科成績："))
total = score1 + score2 + score3
print("Name:" + name + '\n' + "Id:" + std_id + '\n' +
        "Total:" + str(total) + '\n' + "Average:" + str(int(total/3)))
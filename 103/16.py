"""
賓果遊戲

假設一個簡單的兩人賓果遊戲，每位玩家各自輸入一個九宮格，九個數字N1,N2,…N9，
且Ni!=Nj當i!=j，而1<=Ni, Nj<=9，1<=i, j<=9。

N1 N2 N3
N4 N5 N6
N7 N8 N9

電腦從1~9的整數中選三個數字C1、C2、C3，且Ci!=Cj當i!=j，而1<=Ci, Cj<=9, 且 1<=i, j<=3。

獲勝情況有三種，第一位玩家贏，第二位玩家贏、和平手。

當這三個數字，只在一位玩家的九宮格中，成一條水平線，如上圖的N1,N2,N3、垂直線，如圖中的N1,N4,N7，
或對角線，如圖中的N1,N5,N9，則該玩家獲勝。否則平手。
請寫出一個程式，展現電腦判斷此兩人遊戲獲勝情況。

輸入說明:
輸入多組測試案例，每個測試案例為一次賓果遊戲，格式：
第一行為九個數值介於1到9且相異的整數，每個數字間隔一個空格，表示第一位玩家填寫的九宮格，對應圖中N1,N2,…N9。
第二行為九個數值介於1到9且相異的整數，每個數字間隔一個空格，表示第二位玩家填寫的九宮格，對應圖中N1,N2,…N9。
第三行為三個數值介於1到9且相異的整數，每個數字間隔一個空格，表示電腦選擇的三個數字。
每一組測試案例以 0 間隔。
最後以 -1 結束。

輸出說明:
每一行為每一個測試案例的執行結果，即每一場賓果遊戲的獲勝情形。
若為玩家一獲勝，顯示 Player1 wins；
若為玩家二獲勝，顯示 Player2 wins；
若平手，則顯示 Draw。

Sample Input:
1 2 3 4 5 6 7 8 9
9 8 7 6 5 4 3 2 1
1 2 3
0
1 4 2 5 6 7 3 8 9
9 8 4 7 6 3 5 2 1
2 7 9
0
9 4 2 5 6 1 3 8 7
9 8 4 3 6 7 5 2 1
9 4 8
-1

Sample Output:
Draw
Player1 wins
Player2 wins
"""


Player1 = []    #  用於儲存賓果盤
Line1 = []      #  用於儲存每條線尚未中獎的數字個數
Player2 = []    #  用於儲存賓果盤
Line2 = []      #  用於儲存每條線尚未中獎的數字個數
count = 1
Result = []
#  印出賓果盤，每3個數字換行

def game(get,store,give):        
    
    global Bingo      #  用於判斷是否連線的變數
    Bingo = 1
    #  將每條線尚未中獎的數字個數預設為3
    for k in range(8):
        store.append(3)   
        
    for i in range(3):    
        #  若中獎號碼在某直排
        for check_column in range(3):
            if(get.index(give[i]) % 3 == check_column):
                store[check_column] -= 1
        #  若中獎號碼在某橫排
        for check_row in range(3):
            if(get.index(give[i]) // 3 == check_row):
                store[check_row+3] -= 1
        #  若中獎號碼在斜排
        if(get.index(give[i]) == 4):
            store[6] -= 1
            store[7] -= 1
        elif(get.index(give[i]) % 4 == 0):
            store[6] -= 1
        elif(get.index(give[i]) % 2 == 0):
            store[7] -= 1        
        
        #  判斷是否連線(若連線則變數Bingo == 0)
        for l in range(8):
            Bingo *= store[l]
                       
    if Bingo ==0:
        return Bingo    
   
    else:    
        return Bingo   
                

while 1:
    
    Player1 = list(map(int, input().split()))
    Player2 = list(map(int, input().split()))
    Choice = list(map(int,input().split()))  #  由使用者輸入中獎號碼    
    Line1.clear()            #  清除用於儲存每條線尚未中獎的數字個數
    Line2.clear()    
    p1 = game(Player1,Line1,Choice) 
    judge1 = Bingo

    p2 = game(Player2,Line2,Choice)   
    judge2 = Bingo
    
    if (judge1 is 0 and judge2 is 0):
        Result.append('Draw') 
        
    elif(judge1 is 0 and judge2 is not 0):
        Result.append('Player1 wins')
    elif(judge1 is not 0 and judge2 is 0):
        Result.append('Player2 wins')
    else:    
        Result.append('Draw')
    again = input()

    
    if again == '0':
        count = count + 1
        continue
    
    elif again == '-1':       
        break
for i in range(count):
    print(Result[i])        
        

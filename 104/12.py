"""
104012 用LinkedList 實作 Queue
"""


###Linklist的節點
class Node:
    value = 0  ### 節點的值
    nextNode = None  ##存放下一個節點

    def __init__(self, value):
        self.value = value


### LinkedList 實作
class LinkedList:
    name = ''
    count = 0
    node = None
    firstNode = None
    lastNode = None

    ###設定LinkedList的名子
    def __init__(self, name):
        self.name = name

    ###檢查LinkedList是否為空
    def IsListEmpty(self):
        if self.count == 0:
            return True

    ###在最"後"面新增node
    def AddLast(self, value):
        node = Node(value)  ###new a node

        if self.IsListEmpty():  ###如果是空的 那First節點會等於新增的
            self.firstNode = node
        else:  ###如果不是空的就把新增的節點放在Last節點後面
            self.lastNode.nextNode = node
        self.lastNode = node  ##把新節點標記成Last
        self.CalculationCount(1)

    ###刪除第一個
    def DeleteFirst(self):
        if not self.IsListEmpty():
            node = self.firstNode.nextNode  ###第一個的 NextNode
            self.firstNode = node  ###第一個變成原本第一個的NextNode
            self.CalculationCount(-1)  ###List 長度減1

    ###印出List元素
    def PrintList(self):
        outString = ''
        current = self.firstNode
        while (current != None):
            outString = outString + str(current.value) + ' '
            current = current.nextNode  ###nextNode 是下一個
        return outString

    ###控制List長度
    def CalculationCount(self, number):
        self.count = self.count + number


###Queue 使用LinkedList 並且管理LinkedList
class LinkedListQueue():
    linkedListList = []  ###linkedlist 群

    ###新增一個LinkedList
    def CreateLinkedList(self, name):
        self.linkedListList.append(LinkedList(name))  ###new one LinkedList

    ###新增到最元素到某List的最後面
    def Enqueue(self, name, value):
        list = self.GetLinkedLisByName(name)
        list.AddLast(value)

    ###刪除某個LinkedList的第一個元素
    def Dequeue(self, name):
        if self.CheckQueueIsEmpty():
            print("Queue is empty ")
            return
        list = self.GetLinkedLisByName(name)
        list.DeleteFirst()

    ###確認LinkedList群裡面是否有List
    def CheckQueueIsEmpty(self):
        for i in self.linkedListList:
            if i.IsListEmpty():
                return True

    ###確認某個名子的LinkedList存不存在
    def CheckListExist(self, name):
        if self.GetLinkedLisByName(name) != None:
            return True
        print("Queue %s isn't exist" % (name))
        return False

    ###印出全部List和全部List的元素
    def PrintQueue(self):
        self.PrintStar()
        if len(self.linkedListList) == 0:
            print ("Isn't have any queue ")
        for i in self.linkedListList:
            if i.IsListEmpty():
                print ("Queue Name:%s Queue Size:%d Queue Element:Queue is empty" % (i.name, i.count), end=' ',)
            else:
                print ("Queue Name:%s Queue Size:%d Queue Element:%s" % (i.name, i.count, i.PrintList()), end=' ')
            print("")
        self.PrintStar()

    ###依照List名子拿到List
    def GetLinkedLisByName(self, name):
        for i in self.linkedListList:
            if name == i.name:
                return i
        return None

    ###合併兩個List 將B接在A後面 接完並且刪除B
    def MergeQueue(self, ListA, ListB):
        ListA = self.GetLinkedLisByName(ListA)
        ListB = self.GetLinkedLisByName(ListB)

        ###把B的值一個一個拿出來加到A的最後一個
        for i in range(ListB.count):
            ListA.AddLast(ListB.firstNode.value)
            ListB.DeleteFirst()

    ###用名子找尋 並刪除
    def DeleteQueue(self, name):
        list = self.GetLinkedLisByName(name)
        self.linkedListList.remove(list)

    ###印出間隔
    def PrintStar(self):
        print("**************************************** ")


def main():
    while True:
        linkedListQueue = LinkedListQueue()
        order = int(input())
        if (order == 1):  ###功能1 新增LinkedList
            name = input().strip()
            linkedListQueue.CreateLinkedList(name)
        if (order == 2):  ###功能2 新增某LinkedList元素
            name = input().strip()
            if not linkedListQueue.CheckListExist(name):  ###先確認LinkedList在不在 不在就不往下做
                continue
            value = int(input())
            linkedListQueue.Enqueue(name, value)
        if (order == 3):  ###功能3 刪除某LinkedList元素
            name = input().strip()
            linkedListQueue.Dequeue(name)
        if (order == 4):  ###功能4 將兩個LinkedList串接
            name1 = input().strip()
            name2 = input().strip()
            if not linkedListQueue.CheckListExist(name1) or not linkedListQueue.CheckListExist(name2):  ###先確認LinkedList在不在 不在就不往下做
                continue
            linkedListQueue.MergeQueue(name1, name2)
            linkedListQueue.DeleteQueue(name2)  ###合併完要刪掉 第二個List 題目要求
        if (order == 5):  ###功能5 印出LinkedList元素
            linkedListQueue.PrintQueue()
        if (order == 6):  ###功能6 離開程式
            break


main()

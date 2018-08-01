class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class CircularQueue:

    # Constructor
    def __init__(self):
        self.queue = list()
        self.head = 0
        self.tail = 0
        self.maxSize = 5

    # Adding elements to the queue
    def enqueue(self, data):
        self.queue.append(data)
        self.tail = (self.tail + 1) % self.maxSize

    # Removing elements from the queue
    def dequeue(self):
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.maxSize
        return data

    # Calculating the size of the queue
    def size(self):
        if self.tail >= self.head:
            return (self.tail - self.head)
        return (self.maxSize - (self.head - self.tail))


lst = []
s = Stack()
Select = input()
if Select == '1':
    s = Stack()
    while 1:
        mov = input().split(' ')
        if mov[0] == '1':
            if s.size() > 4:
                print("FULL")
                break
            else:
                s.push(int(mov[1]))
        elif mov[0] == '2':
            if s.size() == 0:
                print("EMPTY")
                break
            else:
                print(s.pop(), s.size())
        elif mov[0] == '3':
            while s.isEmpty() is False:
                # print(s.pop())
                lst.append(s.pop())
            lst = reversed(lst)
            print(*lst)
            break

elif Select == '2':
    q = CircularQueue()
    while 1:
        mov = input().split(' ')
        if mov[0] == '1':
            if q.size() < 4:
                q.enqueue(int(mov[1]))
            else:
                print("FULL")
                break
        elif mov[0] == '2':
            if q.size() > 0:
                q.dequeue()
            else:
                print("EMPTY")
                break
        elif mov[0] == '3':
            while q.size() != 0:
                lst.append(q.dequeue())
            print(*lst)
            break 
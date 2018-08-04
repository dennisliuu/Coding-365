# Linked-list
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
# Stack
class ImplementStack:
    def __init__(self):
        self.head = None
 
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            _node = Node(data)
            _node.next = self.head
            self.head = _node
 
    def pop(self):
        if self.head is None:
            return None
        else:
            _popped = self.head.data
            self.head = self.head.next
            return _popped
 
stack = ImplementStack()
answers = []
while True:
    do = input().split()
    operation = do[0]
    if operation is '1':
        stack.push(int(do[1]))
    elif operation is '2':
        popped = stack.pop()
        answers.append('The Stack is empty') if popped is None else answers.append('The data %d is pop' % int(popped))
    elif operation is '3':
        break
for i in answers:
    print(i)

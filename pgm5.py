# IMPLEMENTATION OF STACK ADT
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.top = None
        self.ctr = 0

    def Push(self, data):
        node = Node(data)
        if self.top is None:
            self.head = node
            self.top = node
        else:
            node.next = self.top
            self.top = node
        print("Node pushed to stack:", data)
        self.ctr += 1

    def Pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            print("Deleted from Stack:", self.top.data)
            if self.head == self.top:
                self.head = self.top = None
            else:
                temp = self.head
                while temp.next is not self.top:
                    temp = temp.next
                temp.next = None
                self.top = temp
            self.ctr -= 1

    def Traverse(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            while temp:
                print(temp.data)
                temp = temp.next

def Menu():
    print("**************Stack Menu***************")
    print("1. Push")
    print("2. Pop")
    print("3. Traverse")
    print("4. Number of nodes")
    print("5. Exit")
    ch = int(input("Enter choice: "))
    return ch

s = Stack()
print("**************Stack*****************")
while True:
    ch = Menu()
    if ch == 1:
        data = input("Enter data: ")
        s.Push(data)
    elif ch == 2:
        s.Pop()
    elif ch == 3:
        s.Traverse()
    elif ch == 4:
        print("Number of nodes:", s.ctr)
    elif ch == 5:
        print('Quit')
        break

# IMPLEMENTATION OF QUEUE ADT
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print("Initial queue")
print(queue)
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print("\nQueue after removing elements")
print(queue)
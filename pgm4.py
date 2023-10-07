# IMPLEMENTATION OF LINKED LIST
class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def printLL(self):
        print("The data elements in the linked list are:")
        current = self.head
        while current:
            print(current.data)
            current = current.next


# Create a linked list and insert elements
LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)

# Print the linked list
LL.printLL()

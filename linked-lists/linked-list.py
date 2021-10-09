

class Node():
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self, head = None):
        self.head = head
        self.tail = head

    def insertBeforeHead(self, val):
        nn = Node(val)
        nn.next = self.head
        self.head = nn
    
    def insertAfterTail(self, val):
        nn = Node(val)
        self.tail.next = nn
        self.tail = self.tail.next
    
    def findLength(self):
        l = 0
        temp = self.head
        while temp:
            l += 1
            temp = temp.next
        return l
    
    def print(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

ll = LinkedList(Node(5))
ll.insertBeforeHead(1)
ll.insertAfterTail(10)
print(ll.findLength)
ll.print()



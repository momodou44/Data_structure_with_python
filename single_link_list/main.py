class Node:
    def __init__(self, data) :
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        tmp = self.head
        if self.head is None:
            print("The List is Empty")
        while tmp:
            print(tmp.data, "-->", end=" ")
            tmp = tmp.next

    def insert_at_beginning(self, nb):
        tmp = self.head
        self.head = nb
        nb.next = tmp
    def insert_at_end(self, ne):
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        tmp.next= ne
    def insert_at_position(self,np,p):
        tmp = self.head
        for i in range(p-1):
            tmp = tmp.next
        np.next = tmp.next
        tmp.next = np
        

l = SingleLinkedList()
n1 = Node(20)
n2 = Node(30)
n3 = Node(40)
nb = Node(10)
ne = Node(50)
np = Node(35)

l.head = n1
n1.next = n2
n2.next = n3

l.insert_at_position(np,1)
l.display()
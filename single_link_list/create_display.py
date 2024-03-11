class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # adresse of next node


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        tmp = self.head
        if self.head is None:
            print("The list is empty")
        while tmp:
            print(tmp.data, "-->", end=" ")
            tmp = tmp.next




n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
l = SingleLinkedList()
l.head = n1
n1.next = n2
n2.next = n3

l.display()
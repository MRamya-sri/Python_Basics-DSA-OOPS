class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(3)
node2 = Node(98)
node3 = Node(43)
node4 = Node(67)


node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3

#traversing forward
def traversingForward(head):
    currentnode = head
    while currentnode:
        print(currentnode.data, end = "->")
        currentnode = currentnode.next
    print("null")

#traversing backward
def traversingBackward(tail):
    currentnode = tail
    while currentnode:
        print(currentnode.data, end="->")
        currentnode = currentnode.prev
    print("null")


#calling functions
print("Traversing Forward:\n")
print(traversingForward(node1))

print("/nTraversing Backward:\n")
print(traversingBackward(node4))
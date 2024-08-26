class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(3)
node2 = Node(5)
node3 = Node(1)
node4 = Node(2)

node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3
node4.next = node1

node1.prev = node4

def traverseForward(head):
    currentnode = head
    startnode = head
    print(currentnode.data, end = "->")
    currentnode = currentnode.next

    while currentnode != startnode:
        print(currentnode.data, end = "->")
        currentnode = currentnode.next
    print("....")
    return head

def traverseBackward(tail):
    currentnode = tail
    startnode = tail
    print(currentnode.data, end = "->")
    currentnode = currentnode.prev

    while currentnode != startnode:
        print(currentnode.data, end = "->")
        currentnode = currentnode.prev
    print("....")
    return tail

print("Forward Traverse of circular list: ")
traverseForward(node1)

print("Backward Traverse of circular list: ")
traverseBackward(node4)
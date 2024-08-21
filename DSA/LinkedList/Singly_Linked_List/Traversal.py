class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseandPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end="->")
        currentNode = currentNode.next
    print("null")


node1 = Node(5)
node2 = Node(78)
node3 = Node(43)
node4 = Node(2)
node5 = Node(12)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseandPrint(node1)
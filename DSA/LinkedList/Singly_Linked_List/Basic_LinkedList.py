class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

# creating nosed
node1 = Node(3)
node2 = Node(21)
node3 = Node(87)
node4 = Node(9)
node5 = Node(55)

# link/next 
node1.next = node2
node2.next = node3
node3.next = node4

#traversing
currentNode = node1
while currentNode: #until currentNode is not equal to null
    print(currentNode.data, end = "->")
    currentNode = currentNode.next

print("null")


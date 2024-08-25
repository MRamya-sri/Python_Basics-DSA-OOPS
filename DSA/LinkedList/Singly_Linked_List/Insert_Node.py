class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseandPrint(head):
    currentnode = head
    while currentnode:
        print(currentnode.data, end = "->")
        currentnode = currentnode.next
    print("null")


def insertNodeAtPosition(head, newNode, position):

    if position == 1:
        newNode.next = head
        return head
    
    currentnode = head

    for _ in range(position-2):
        if currentnode is None:
            break
        currentnode = currentnode.next

    newNode.next = currentnode.next

    currentnode.next = newNode

    return head




node1 = Node(7)
node2 = Node(3)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

print("Original list:")
traverseandPrint(node1)

# insert 
newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 2)
print("\nAfter insertion:")
traverseandPrint(node1)
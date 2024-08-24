
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


def delete_specific_node(head, nodeToDelete):

    if head == nodeToDelete:
        return head.next
    
    currentnode = head
    while currentnode.next and currentnode.next != nodeToDelete:
        currentnode = currentnode.next

    if currentnode.next is None:
        return head
    
    currentnode.next = currentnode.next.next

    return head



node1 = Node(7)
node2 = Node(56)
node3 = Node(3)
node4 = Node(8)
node5 = Node(21)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deleting: ")
print(traverseandPrint(node1))

# removing or deleting
node1 = delete_specific_node(node1, node4)
print("After Deleting :")
print(traverseandPrint(node1))

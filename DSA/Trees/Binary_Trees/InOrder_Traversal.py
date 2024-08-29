class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('R')
nodeA= TreeNode('A')
nodeB= TreeNode('B')
nodeC= TreeNode('C')
nodeD= TreeNode('D')
nodeE= TreeNode('E')
nodeF= TreeNode('F')
nodeG= TreeNode('G')


root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

def InOrderTraversal(node):
    if node is None:
        return
    InOrderTraversal(node.left)
    print(node.data, end = ",")
    InOrderTraversal(node.right)

print("Inorder Traversal of Tree is : \n")
InOrderTraversal(root)

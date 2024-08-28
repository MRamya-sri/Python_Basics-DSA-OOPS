class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        popped_node = self.top
        self.top = self.top.next
        return popped_node.value
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.top.value
        
    def size(self):
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def print(self):
        current = self.top
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Stack Values:")
            while current:
                print(current.value)
                current = current.next

# Creating an instance 
MyStack = Stack()

# Push
MyStack.push(10)
MyStack.push('CD')
MyStack.push('EF')
MyStack.push('GH')
MyStack.push('IG')
MyStack.print()

# Size
print("Size : ", MyStack.size())

# Pop
print("Popped Element:", MyStack.pop())

# Peek
print("Top Element is:", MyStack.peek())

# Size after popping
print("Size after popping element:", MyStack.size())

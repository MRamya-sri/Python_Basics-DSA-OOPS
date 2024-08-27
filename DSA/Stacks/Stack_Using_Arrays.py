class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)

    def isempty(self):
        return len(self.stack) == 0
    
    def pop(self):
        if self.isempty():
            return "Stack is Empty"
        return self.stack.pop()

    def peek(self):
        if self.isempty():
            return "Stack is empty"
        return self.stack[-1]

    def size(self):
        return len(self.stack)


MyStack = Stack() #creating a instance of a Class

MyStack.push('A')
MyStack.push('B')
MyStack.push('C')
MyStack.push('D')

print("Stack: ", MyStack.stack)

print("popped top element: ", MyStack.pop())

print("Peek Element is: ", MyStack.peek())

print("isEmpty :", MyStack.isempty())

print("Current size of Stack: ", MyStack.size())

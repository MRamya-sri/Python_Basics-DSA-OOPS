stack = []

#push
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')
print("Stack Elements:", stack)

#pop
element = stack.pop()
print("The Top Element is popped out : ", element)

#peek
peek = stack[-1]
print("The Peek value is: ", peek)

#isempty
isempty = not bool(stack)
print("isempty :",isempty)

#size
size = len(stack)
print("size: ", size)
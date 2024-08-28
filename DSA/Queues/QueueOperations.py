#array queue
queue = []

#Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
queue.append('D')
queue.append('E')
queue.append('F')
print("Queue: ", queue)


#Dequeue
dequeue = queue.pop(0)
print("Dequeued value: ", dequeue)

#peek
peek = queue[0]
print("Peek value:", peek)

#isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

#size
size = len(queue)
print("Size :", size)

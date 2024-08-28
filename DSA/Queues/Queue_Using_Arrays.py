class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0
    
    def enqueue(self,element):
        return self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.queue.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.queue[0]
        
    def size(self):
        return len(self.queue)
    
# create an instance of a class        
MyQueue = Queue()

MyQueue.enqueue('WEB')
MyQueue.enqueue('JAVA')
MyQueue.enqueue('XML')
MyQueue.enqueue('HTML')

#print array of queue
print("QUEUE: ", MyQueue.queue)

#dequeue element
print("Dequeue of Element: ", MyQueue.dequeue())

#size
print("Size: ", MyQueue.size())

#isEmpty
print("isEmpty? : ", MyQueue.isEmpty())
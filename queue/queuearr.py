class Queue:
    data = []
    def enqueue(self,value):
        self.data.append(value)
    def dequeue(self):
        item = self.data.pop(0)
        return item
    def peek(self):
        return self.data[len(self.data)-1]
    
    def printQueue(self):
        print(self.data)

qu = Queue()
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
qu.printQueue()
print("removing",qu.dequeue())
print("removing",qu.dequeue())
qu.printQueue()

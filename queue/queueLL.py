class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    head = None
    tail = None
    size = 0

    def peek(self):
        if(self.head):
            return self.head.data
        else:
            raise Exception("empty Queue")

    def enqueue(self,data):
        newNode = Node(data)
        if(not self.head):
            self.head = newNode
            self.tail = newNode
            self.size+=1
        else:
            if(self.tail):
                self.tail.next = newNode
                self.tail = newNode
            self.size+=1
    
    def dequeue(self):
        item = None
        if(not self.head):
            raise Exception("no element found!")
        else:
            item = self.head.data
            self.head = self.head.next
            self.size -=1
        return item

    def printQueue(self):
        dataLis = []
        currentNode = self.head
        while(currentNode):
            dataLis.append(currentNode.data)
            currentNode = currentNode.next
        print(dataLis)


qu = Queue()
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
qu.printQueue()
print(qu.dequeue())
print(qu.dequeue())
qu.printQueue()

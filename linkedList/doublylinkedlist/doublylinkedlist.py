class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DLinkedList:
    head = None
    size = 0
    tail = None
    # get to specific location on linked list
    def traverseToIndex(self,loc,assending=True):
        if(assending):
            currentNode = self.head
            for _ in range(0,loc):
                currentNode = currentNode.next

        else:
            currentNode = self.tail
            for _ in range(0,loc):
                currentNode = currentNode.prev

        return currentNode

    # add data to the back
    def append(self,data):
        if(not self.head):
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
        else:
            currentNode = self.traverseToIndex(self.size)
            if(currentNode):
                newNode = Node(data, prev=currentNode)
                currentNode.next = newNode
                self.tail = newNode 
                self.size+=1
            else:
                raise Exception("some error occured")


    # add data to front
    def prepend(self,data):
        if(not self.head):
            newNode = Node(data)
            self.data = newNode
            self.tail = newNode
        else:
            first = self.head
            newNode = Node(data,first)
            first.prev = newNode
            self.head = newNode
        self.size+=1
    
    # print the data in form of list
    def printLinkedList(self,assending=True):
        dataLis = []
        if(assending):
            currentNode = self.head
        else:
            currentNode = self.tail
        while(currentNode):
            dataLis.append(currentNode.data)
            if(assending):
                currentNode = currentNode.next
            else:
                currentNode = currentNode.prev
        print(dataLis)

    # look for specific item if not found return None
    def lookup(self,searchStuff):
        currentNode = self.head
        count = 0
        while currentNode:
            if(currentNode.data == searchStuff):
                return count
            else:
                count+=1
                currentNode = currentNode.next
    
   
    # insert at specific location
    def insert(self,loc,data):
        if(not self.head or loc > self.size):
            raise Exception("linked list out of bound")
        else:
            currentNode = self.traverseToIndex(loc)
            if (currentNode):
                rightHalf = currentNode.next
                if(rightHalf):
                    newNode = Node(data,rightHalf,currentNode)
                    rightHalf.prev = newNode
                    currentNode.next = newNode
                    self.size+=1
            else:
                raise Exception("some error occured")

    # remove an element from location
    def remove(self, loc):
        currentNode = self.traverseToIndex(loc)
        leftNode = self.traverseToIndex(loc-1)
        if(currentNode and leftNode):
            rightNode = currentNode.next
            if(rightNode):
                leftNode.next = rightNode
                rightNode.prev = leftNode
        else:
            raise Exception("some thing went wrong")

dll = DLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.printLinkedList()
dll.insert(2,200)
dll.printLinkedList(False)
dll.printLinkedList()
print("deleting stuff")
dll.remove(2)
dll.printLinkedList()
dll.printLinkedList(False)
dll.prepend(1000)
dll.printLinkedList()
dll.printLinkedList(False)

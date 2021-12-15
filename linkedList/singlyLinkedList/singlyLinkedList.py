class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SLinkedList:
    head = None
    size = 0
    # get to specific location on linked list
    def traverseToIndex(self,loc):
        currentNode = self.head
        for _ in range(0,loc):
            currentNode = currentNode.next

        return currentNode

    # add data to the back
    def append(self,data):
        if(not self.head):
            self.head = Node(data)
        else:
            currentNode = self.traverseToIndex(self.size)
            if(currentNode):
                currentNode.next = Node(data)
                self.size+=1
            else:
                raise Exception("some error occured")


    # add data to front
    def prepend(self,data):
        if(not self.head):
            self.head = Node(data)
        else:
            first = self.head
            newNode = Node(data,first)
            self.head = newNode
            
        self.size+=1
    
    # print the data in form of list
    def printLinkedList(self):
        currentNode = self.head
        dataLis = []
        while(currentNode):
            dataLis.append(currentNode.data)
            currentNode = currentNode.next
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
                currentNode.next = Node(data,rightHalf)
                self.size+=1
            else:
                raise Exception("some error occured")

    # remove an element from location
    def remove(self, loc):
        currentNode = self.traverseToIndex(loc)
        leftNode = self.traverseToIndex(loc-1)
        if(currentNode and leftNode):
            rightNode = currentNode.next
            leftNode.next = rightNode
        else:
            raise Exception("some thing went wrong")
            






ss = SLinkedList()
ss.append(3)
ss.append(4)
ss.append(5)
ss.printLinkedList()
print("prepending")
ss.prepend(10)
ss.printLinkedList()
ss.insert(1,20)
ss.insert(1,40)
ss.printLinkedList()
print(f"stuff is found at {ss.lookup(100)}")
ss.remove(3)
ss.printLinkedList()

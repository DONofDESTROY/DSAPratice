class Node:
    def __init__(self,data, next=None):
        self.data = data
        self.next = next


class Stack:
    top = None
    size = 0
    head = None

    def push(self,data):
        newNode = Node(data)
        if(not self.head or not self.top):
            self.head = newNode
            self.size+=1
            self.top = newNode 
        else:
            self.top.next = newNode
            self.top = newNode
            self.size+=1

    def peek(self):
        if(self.top):
            return self.top.data
        else:
            raise Exception("List is empty!")
    
    def pop(self):
        currentNode = self.head
        while(currentNode.next != self.top):
            currentNode = currentNode.next
        if(self.top):
            item = self.top.data
            self.top = currentNode
            currentNode.next = None
            return item
        else:
            raise Exception("list is empty!")


    def printStack(self):
        data = []
        currentNode = self.head
        while(currentNode):
            data.append(currentNode.data)
            currentNode = currentNode.next
        print(data)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.printStack()
print(stack.pop())
print(stack.peek())
stack.printStack()


            


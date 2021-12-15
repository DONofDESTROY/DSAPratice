class Stack:
    arr = []
    def push(self,data):
        self.arr.append(data)
    def pop(self):
        return self.arr.pop()
    def peek(self):
        return self.arr[len(self.arr)-1]
    def printStack(self):
        print(self.arr)

stack = Stack()
stack.push(20)
stack.push(30)
stack.push(40)
stack.printStack()
stack.pop()
stack.pop()
stack.printStack()


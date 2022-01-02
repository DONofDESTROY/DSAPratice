import json
class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    root = None
    def insertNode(self,value):
        currentNode = self.root
        if(not currentNode):
            self.root = Node(value)
        else:
            while(currentNode):
                if(currentNode.value > value):
                    if(currentNode and not currentNode.left):
                        currentNode.left = Node(value)
                        return
                    currentNode = currentNode.left
                else:
                    if(currentNode and not currentNode.right):
                        currentNode.right = Node(value)
                        return
                    currentNode = currentNode.right

    def lookup(self,value):
        currentNode = self.root
        if(not currentNode):
            raise Exception("Empty Tree!")
        else:
            while(currentNode):
                if(currentNode.value > value):
                    if(currentNode.value == value):
                        return True
                    currentNode = currentNode.left
                else:
                    if(currentNode.value == value):
                        return True
                    currentNode = currentNode.right
        return False

    def deleteNode(self,value):
        currentNode = self.root
        parentNode = self.root
        if(not currentNode):
            raise Exception("Empty Tree!")
        else:
            while(currentNode):
                if(currentNode.value > value):
                    if(currentNode.value == value):
                        break
                    parentNode = currentNode
                    currentNode = currentNode.left
                else:
                    if(currentNode.value == value):
                         break
                    parentNode = currentNode
                    currentNode = currentNode.right
            # if currentNode have no left child
            # needs to be probly learned and implemented
            if(currentNode and parentNode):
                if(not currentNode.left and not currentNode.right):
                    currentNode = None
                elif(not currentNode.right):
                    parentNode.left = currentNode.left
            # currentNode has right
                 

                



def treeToJson(root):
    currentNode = root
    dict = {'value':currentNode.value}
    dict['left'] = None if(not currentNode.left) else treeToJson(currentNode.left)
    dict['right'] = None if (not currentNode.right) else treeToJson(currentNode.right)
    return dict
    


tree = BinarySearchTree()
arr = [41,20,29,32,11,65,50,91,72,99,10]
for i in arr:
    tree.insertNode(i)
# value = json.dumps(treeToJson(tree.root))
# print(value)
print(tree.lookup(100))
print(tree.lookup(99))
tree.deleteNode(11)
value = json.dumps(treeToJson(tree.root))
print(value)

class Node:
    def __init__(self,isEnd=False):
        self.children = {}
        self.isEnd = isEnd

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd
    
    def startsWith(self,word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


obj = Trie()
obj.insert("apple")
obj.insert("apartment")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.search("apartment"))
print("startwith")
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))

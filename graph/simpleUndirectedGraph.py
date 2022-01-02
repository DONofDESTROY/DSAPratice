class UndirectedGraph:
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}
    
    def addVertex(self,value):
        self.adjacentList[value] = []
        self.numberOfNodes+=1

    def addEdge(self,start,end):
        self.adjacentList[start].append(end)
        self.adjacentList[end].append(start)

    def printGraph(self):
        for i in self.adjacentList.items():
            print(f"{i[0]} -->",end="")
            for j in i[1]:
                print(j, end=" ")
            print()
            


graph = UndirectedGraph()
graph.addVertex(1)
graph.addVertex(2)
graph.addVertex(3)
graph.addVertex(4)
graph.addVertex(5)
graph.addVertex(6)
graph.addVertex(7)
graph.addVertex(8)

graph.addEdge(1,2)
graph.addEdge(1,3)
graph.addEdge(2,3)
graph.addEdge(2,5)
graph.addEdge(7,2)
graph.addEdge(4,7)
graph.addEdge(5,3)
graph.addEdge(7,8)
graph.addEdge(8,1)

graph.printGraph()

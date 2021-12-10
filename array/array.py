# reinventing the weel to check what i learned today
#useless implementation working model of array
class array():
    data = {}
    size = 0
    """
    return the element from array
    """
    def at(self,loc):
        return self.data[loc]

    """
    add element to back of an array
    """
    def pushBack(self,item):
        self.data[self.size] = item; 
        self.size+=1

    """
    print array
    """
    def printArr(self):
        print("[",end=" ")
        for i in self.data:
            if(i+1 is not self.size):
                print(self.data[i],end=", ")
            else:
                print(self.data[i],end=" ")
        print("]")

    """
    remove element from last and return it
    """
    def popBack(self):
        element = self.data[self.size-1]
        del self.data[self.size-1]
        self.size -=1
        return element

    """
    insert an element at given locaiton
    """
    def insert(self, loc, item):
        self.shift(loc)
        self.data[loc] = item
        self.size+=1

    """
    deletes at spefici locataion
    """ 
    def deleteAt(self, loc):
        return self.unShift(loc)

    """
    shifts element to right
    """
    def unShift(self,loc):
        loct = loc
        item =  self.data[loc]
        for i in range(loct, self.size-1):
                self.data[i]= self.data[i+1]
        del self.data[self.size-1]
        self.size-=1
        return item

    """
    shifts elements to left
    """
    def shift(self, loc):
        for i in range(self.size, loc, -1):
            self.data[i]= self.data[i-1]

arr = array()
arr.pushBack('h')
arr.pushBack('e')
arr.pushBack('l')
arr.pushBack('l')
arr.pushBack('o')
arr.printArr()


#another usesless hashtable implementation
class HashTable():
    def __init__(self, size):
        self.data = [[] for _ in range(size)]

    
    #a method for internal use dont use this outside
    def _hash(self,key):
        return hash(key) % len(self.data)

    # set item ie create / update a key value pair 
    def setItem(self,key, value):
        address = self._hash(key)
        if(not self.getItem(key)):
            KVparis = [key, value];
            if(self.data[address]==None):
                self.data[address] = []
                self.data[address].append(KVparis)
            else:
                self.data[address].append(KVparis)
        else:
            bucket = self.data[address]
            for i in bucket:
                if(i[0]==key):
                    i[1]= value
        

    # returns a key value pair
    def getItem(self, key):
        bucket = self.data[self._hash(key)]
        item = None
        for i in bucket:
            if(i[0]==key):
                item = i[1]
        return item
    # returns all avaliable keys
    def getKeys(self):
        keys = []
        for i in self.data:
            if(i != None):
                for j in i:
                    keys.append(j[0])
        return keys

    # returns all avaliable values
    def getValues(self):
        values = []
        for i in self.data:
            if(i != None):
                for j in i:
                    values.append(j[1])
        return values

ht = HashTable(2)
ht.setItem('grape',1000)
ht.setItem('apple',200)
ht.setItem('something',100)
ht.setItem('something',2000)
print(ht.getItem('applee'))
print(ht.getKeys())
print(ht.getValues())

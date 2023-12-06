from LinkedList.LinkedHashTable import LinkedHashTable

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linkedHT = LinkedHashTable()

    def get(self, key):
        if self.linkedHT.get(key) is None :
            return -1
        
        self.linkedHT.update(key,self.linkedHT.get(key))
        return self.linkedHT.get(key)


    def put(self, key, val):
        if self.linkedHT.get(key) is None :
            if self.linkedHT.size() == self.capacity :
                self.linkedHT.remove(self.linkedHT.tail.prev.key)

        self.linkedHT.add(key,val)

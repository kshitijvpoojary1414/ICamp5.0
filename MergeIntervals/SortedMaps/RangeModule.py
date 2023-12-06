from sortedcontainers import SortedDict,SortedList
class RangeModule:

    def __init__(self):
        self.d = SortedDict()
       
    def addRange(self, left: int, right: int) -> None:
        keys = SortedList(self.d.keys() )
        lIndex = keys.bisect_right(left)
        rIndex = keys.bisect_right(right)
        
        if lIndex != 0 and self.d[keys[lIndex-1]] >= left:
            left = keys[lIndex-1]
        if rIndex != 0 :
            right = max(right, self.d[keys[rIndex-1]])

        for i,key in enumerate(keys) :
            if left <= key <= right :
               del self.d[key]

        self.d[left] = right    
        #print(self.d)

    def queryRange(self, left: int, right: int) -> bool:
        keys = SortedList(self.d.keys())
        left = keys.bisect_right(left)
        #print(self.d)

        if left != 0 and self.d[keys[left-1]] >= right :
            return True 
        return False      

    def removeRange(self, left: int, right: int) -> None:
        
        keys = SortedList(self.d.keys() )
        lIndex = keys.bisect_right(left)
        rIndex = keys.bisect_right(right)
        lVal = 0 if lIndex == 0 else self.d[keys[lIndex-1]]
        rVal = 0 if rIndex == 0 else self.d[keys[rIndex-1]]
        if lIndex != 0 :
            self.d[keys[lIndex-1]] = min(left, lVal)
        if rIndex != 0 and rVal > right :
            self.d[right] = rVal

        for i,key in enumerate(keys) :
            if left < key < right :
                del self.d[key]

        #print(self.d)

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
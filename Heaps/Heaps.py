class MaxHeap :
    def __init__(self) :
        self.heap = []

    def push(self, value) :
        heapq.heappush(self.heap, -1 * value)
    
    def pop(self) :
        return -1*heapq.heappop(self.heap)

    def peek(self) :
        return -1*self.heap[0]
    
    def print(self) :
        print(self.heap)

class MinHeap :
    def __init__(self) :
        self.heap = []

    def push(self, value) :
        heapq.heappush(self.heap,  value)
    
    def pop(self) :
        return heapq.heappop(self.heap)

    def peek(self) :
        return self.heap[0]
    def print(self) :
        print(self.heap)

class MedianFinder:

    def __init__(self):
        self.lower = MaxHeap()
        self.upper = MinHeap()
        self.total = 0

    def addNum(self, num: int) -> None:
        if self.total == 0 :
            self.upper.push(num)

        elif self.total%2 == 0 :
            if num < self.lower.peek() :
                self.upper.push(self.lower.pop())
                self.lower.push(num)
            else :
                self.upper.push(num)
        else :
            if num > self.upper.peek() :
                self.lower.push(self.upper.pop())
                self.upper.push(num) 
            else :
                self.lower.push(num)
        self.total +=1
    def findMedian(self) -> float:
        if self.total %2 ==0 :
            return (self.lower.peek() + self.upper.peek())/2
        else :
            return self.upper.peek()
        

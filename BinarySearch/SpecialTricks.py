class SpecialTricks :
    boundary = 2**31 -1
    def searchArrayOfUnknown(self, reader: 'ArrayReader', target: int) -> int:
        start,end = self.findRangeOfEndPoint(reader)
        end = self.findActualEndpoint(reader,start,end)

        start = 0

        while start <= end :
            mid = start + (end - start)//2 

            if reader.get(mid) < target :
                start = mid + 1
            elif reader.get(mid) > target :
                end = mid - 1 
            else :
                return mid 

        return -1

    def findActualEndpoint(self, reader, start, end) :
        while start <= end :
            mid = start + (end - start)//2 
            print(mid)
            if reader.get(mid) == self.boundary and (mid > start and reader.get(mid-1) == self.boundary) :
                end = mid - 1
            elif reader.get(mid) != self.boundary and (mid + 1 < end and reader.get(mid + 1) != self.boundary) :
                start = mid + 1 
            else :
                return mid 

    
    def findRangeOfEndPoint(self, reader) :
        start = 2

        while reader.get(start) < 2**31 -1 :
            start = start*2 

        return (start//2, start)

    def peakElement(self, arr) :
      start, end = 0, len(arr) - 1
      arr.append(float('-inf'))

      while start <= end :
        mid = start + (end - start) //2 
        left = arr[mid - 1]
        right = arr[mid + 1 ]

        if left < arr[mid] <  right : 
          start = mid + 1
        elif left > arr[mid] > right :
          end = mid - 1 
        elif left < arr[mid] > right : 
          return mid 
        else :
          end = mid -1

      return 0 

    # def squareRoot(self, num) :
    #   start,end = 0, num//2 

    #   while start <= end :
    #     mid = start + (end- start)//2

    #     if mid ** 2 > num :
    #       end = mid - 1
    #     elif mid ** 2 > num :
    #       mid 

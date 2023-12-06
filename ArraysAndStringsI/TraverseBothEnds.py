class TraverseBothEnds : 
    def reverseArray(self, arr) :
        if arr is None or len(arr) = 0 :
            return arr 

        start, end = 0, len(arr) - 1 

        while start < end : 
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return arr

    def squares(self, arr) :
        if arr is None or len(arr) = 0 :
            return arr 

        output = [None]*len(arr)
        oI = len(arr) - 1
        start, end = 0 , len(arr) - 1 

        while start <= end :
            if arr[start]**2 < arr[end] ** 2 :
                output.append(arr[end])
                end -= 1
            else :
                output.append(arr[start])
                start += 1
            oI -= 1
        return output

   def findUnsortedSubarray(self, nums: List[int]) -> int:
        firstDip = None
        firstRise = None

        for i in range(len(nums)-1) :
            if nums[i] > nums[i+1] :
                firstDip = i
                break

        if firstDip is None :
            return 0

        for i in range(len(nums)-1, 0, -1) :
            if nums[i] < nums[i-1] :
                firstRise = i
                break 

        minimum = min(nums[firstDip:firstRise + 1])
        maximum = max(nums[firstDip:firstRise + 1])
        start,end = firstDip, firstRise
        
        for i in range(firstDip,-1,-1) :
            if nums[i] <= minimum :
                break
            start = i
        for i in range(firstRise,len(nums)) :
            if nums[i] >= maximum :
                break
            end = i

        return end - start + 1
        
            
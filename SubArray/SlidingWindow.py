class SlidingWindow :
    def subArraySumTarget(self,arr, target) :
      left = 0
      right = 0
      currentSum = 0 

      while left < len(arr) :
        if left > right :
          right = left 
          currentSum = arr[left]

        if currentSum < target :
          if right + 1 <= len(arr) - 1
            right += 1 
            currentSum += arr[right]
          else :
            break
        elif currentSum > target :  
          currentSum -= start 
          left += 1 
        else :
          return (left,right)

      return -1

    def longestSubstringWithUniqueChars(self, sentence) :
      indexMap = {}
      left, right = 0,0 
      result = 0
      while right < len(sentence) :
        if sentence[right] in indexMap and indexMap[sentence[right]] >= left:
          left = indexMap[sentence[right]] + 1 
        indexMap[sentence[right]] = right 
        result = max(result,right-left + 1)
        right += 1 
      return result

        
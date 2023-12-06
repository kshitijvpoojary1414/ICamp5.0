class PrefixSum :
  def subarrySumZero(self, arr) :
    currentSum = 0
    indexMap = {} 
    for i in range(len(arr)) :
      currentSum = arr[i] 
      if currentSum in indexMap :
        return True 
      elif currentSum == 0 :
        return True 

      indexMap[currentSum] = i 

    return False 

  def subarrySumEqualsK(self, arr, k) :
    currentSum = 0
    indexMap = {0:-1} 
    for i in range(len(arr)) :
      currentSum = arr[i] 
      if currentSum-k in indexMap :
        return True 

      indexMap[currentSum] = i 

    return False 
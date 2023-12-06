class PermutationsAndCombinations :
  def printCombos(self, arr, x) :
    buffer = [None] * x
    result = []
    self.helper(arr, buffer, 0, 0, result)

  def helper(self, arr, buffer, startIndex, bufferIndex, result) :
    if startIndex == len(arr) :
      return 

    if bufferIndex == len(buffer) :
      result.append(buffer[::])
      return 

    for i in range(startIndex, len(arr)) :
      buffer[bufferIndex] = arr[i]
      self.helper(arr, buffer, i + 1, bufferIndex + 1, result)

    def get_letters(self,digit):
        digit = int(digit)
        if digit == 0:
            return []
        elif digit == 1:
            return []
        elif digit == 2:
            return ['a', 'b', 'c']
        elif digit == 3:
            return ['d', 'e', 'f']
        elif digit == 4:
            return ['g', 'h', 'i']
        elif digit == 5:
            return ['j', 'k', 'l']
        elif digit == 6:
            return ['m', 'n', 'o']
        elif digit == 7:
            return ['p', 'q', 'r', 's']
        elif digit == 8:
            return ['t', 'u', 'v']
        elif digit == 9:
            return ['w', 'x', 'y', 'z']

        raise ValueError("Invalid Digit " + str(digit))
   
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0 :
            return []
        buffer = [0]*len(digits)
        result = []
        self.phoneMnemonicsHelper(digits, buffer,0,0, result )
        return result
    def phoneMnemonicsHelper(self, arr, buffer, startIndex, bufferIndex, result) :
        if startIndex == len(arr) :
            result.append(''.join(buffer))
            return 

        values = self.get_letters(arr[startIndex])

        for val in values :
            buffer[bufferIndex] = val 
            self.phoneMnemonicsHelper(arr, buffer, startIndex + 1 , bufferIndex + 1,result)

    def subsets(self, arr) :
      result = []
      buffer = [0]*len(arr)
      self.subsetHelper(arr, 0, 0, buffer, result)
      return result

    def subsetHelper(self, arr, startIndex, bufferIndex, buffer,result) :
      result.append(buffer[:bufferIndex])

      if startIndex == len(arr) :
        return 

      for i in range(startIndex,len(arr) ) :
        buffer[bufferIndex] = arr[i]
        self.subsetHelper(arr, i + 1, bufferIndex + 1, buffer, result)

    def permutations(self, arr) :
      result = []
      buffer = [0]*len(arr)
      isInBuffer = [False]*len(arr)
      self.permutationsHelper(arr, 0, 0, buffer, result)
      return result

    def permutationsHelper(self, arr, isInBuffer, bufferIndex, buffer,result) :
      if bufferIndex == len(buffer) :
        result.append(buffer[::])

      for i in range(0,len(arr) ) :
        if isInBuffer[i] :
          continue
        buffer[bufferIndex] = arr[i]
        isInBuffer[i] = True
        self.subsetHelper(arr, isInBuffer, bufferIndex + 1, buffer, result)
        isInBuffer[i] = False

    def coinChange(self, arr, target) :
      result = [] 
      buffer = []
      currentSum = 0 

      self.coinChangeHelper(arr, startIndex , buffer, currentSum, result, target) :

    def coinChangeHelper(self, arr, startIndex, buffer, currentSum, result, target) :
      if currentSum > target :
        return 

      if currentSum == target :
        result.append(buffer[::])

      for i in range(startIndex, len(arr)) :
        buffer.append(arr[i])
        self.coinChangeHelper(arr, i, buffer, currentSum + arr[i], result, target)
        buffer.pop() 


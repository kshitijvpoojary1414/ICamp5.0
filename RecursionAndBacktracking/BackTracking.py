class BackTracking :
  def pathExists(self, graph) :
    memo = [[None for i in range(len(graph[0]))] for j in range(len(graph))]
    self.backtrack(0,0,graph, memo,(len(graph)-1, len(graph[0])-1)) 

  def backtrack(self, row, col , graph, memo, target) :
    if self.oob(row, col ,graph) :
      return False 

    if row == target[0] and col == target[1] :
      return True 

    if memo[row][col] != None :
      return False 
    memo[row][col] = True

    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

    for neighbor in neighbors :
      nRow = row + neighbor[0]
      nCol = col + neighbor[1]

      if self.backtrack(nRow, nCol, graph, memo, target) :
        return True 
    
    memo[row][col] = False 
    
    return False 

  def oob(self, row, col, graph) :
    if row < 0 or row >= len(graph) or col < 0 or col >= len(graph[0]) :
      return True 
    return False  

  def isInDictionary(self, word):
      return

  def wordBreak(self, s):
      memo = [0]* len(s)
      result = []
      if self.wordBreakHelper(s, 0, memo, result, []) :
          return result
  
  def workBreakHelper(self, s, startIndex, memo, result, wordList) :
    if startIndex == len(s) :
      result.append(wordList[::])
      return True 

    if memo[startIndex] != 0 :
      return False 

    currentWord = "" 

    for i in range(startIndex, len(arr)) :
      currentWord += s[i]

      if self.isInDictionary(currentWord) :
        wordList.append(currentWord)
        if self.wordBreakHelper(s, i+ 1, memo, result,wordList) :
          return True 
        memo[i+1] = 2
        wordList.pop() 

    return False 
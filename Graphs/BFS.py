class BFS :
  def bfs(self, root, target, graph) :
    if root is None :
        return False 

    visited = set([root]) 
    queue = [root]

    while len(queue) > 0 :
        node = queue.pop(0) 
        
        if node == target :
            return True 

        neighbors = graph[node]

        for neighbor in neighbors :
            if neighbor not in visited :
                queue.append(neighbor)
                visited.add(neighbor)
  
    def printLevels(self, root, target, graph) :
      if root is None :
        return [] 

      visited =set([root]) 
      queue = [root, "#"]
      currentLevel = []

      while len(queue) > 0 :
        node = queue.pop() 

        if node == "#" :
          print(currentLevel)
          currentLevel = []
          if len(queue) > 0 :
            queue.append('#')
          continue 

        currentLevel.append(node)

        neighbors = graph[node]

        for neighbor in neighbors :
          if neighbor not in visited :
            queue.append(neighbor)
            visited.add(neighbor)

      return 

  def createWordMap(self, wordList) :
        wordMap = {}

        for word in wordList :
            for i in range(len(word)) :
                key = word[0:i] + "*" + word[i+1:] 
                if key not in wordMap :
                    wordMap[key] = [word]
                else :
                    wordMap[key].append(word)

        return wordMap
    
    def getNeighbors(self,word, wordMap) :
        neighbors = []

        for i in range(len(word)) :
            key = word[0:i] + "*" + word[i+1:]
            if key in wordMap :
                neighbors += wordMap[key]

        return neighbors
        
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord :
            return 0

        wordMap = self.createWordMap(wordList)

        visited = set(beginWord)
        queue = [(beginWord,1)]
        while len(queue) > 0 :
            node,level = queue.pop(0)
            if node == endWord :
                return level

            neighbors = self.getNeighbors(node, wordMap)

            for neighbor in neighbors :
                if neighbor not in visited :
                    queue.append((neighbor, level + 1))
                    visited.add(neighbor)

        return 0

    
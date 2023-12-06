class TrieNode :
  def __init__(self) :
    self.children = {}
    self.isWord = False

class Trie :
  def __init__(self) :
    self.root = TrieNode()

  def add(self, word) :
    current = self.root 

    for char in word :
      if char not in current.children :
        current.children[char] = TrieNode() 
      current = current.children[char]

    current.isWord = True 

  def search(self, word) :
    current = self.root 

    for char in word :
      if char not in current.children :
        return False
      current = current.children[char]

    return current.isWord 

  def remove(self, word) :
    if word is None or len(word) == 0 :
      return False 
    
    lastNode = self.getLastNode(word)

    lastNode.isWord = False 

    if len(lastNode.children) > 0 :
      return 

    self.removeLastNodeWithMultipleChildren(self, word)

  def removeLastNodeWithMultipleChildren(self, word) :
    current = self.root 
    lastNodeWithMultipleChildren = self.root 
    toDelete = word[0]

    for i,char in enumerate(word) :
      if char not in current :
        return False 

      current = current[char]

      if current.isWord or len(current.children) > 1 :
        lastNodeWithMultipleChildren = current
        toDelete = word[i+1]

    del lastNodeWithMultipleChildren.children[toDelete]
 

  def getLastNode(self,word) :
    current = self.root 

    for char in word :
      if char not in current.children :
        return False
      current = current.children[char]

    return current 

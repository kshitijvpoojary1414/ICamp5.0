class RecordAndMoveOn :
  def firstOccurence(self, value) :
    current = self.root 
    result = None 

    while current is not None :
      if value < current.value :
        current = current.left 
      elif value > current.value :
        current = current.right 
      else :
        result = current.val 
        current = current.left 

    return result
    
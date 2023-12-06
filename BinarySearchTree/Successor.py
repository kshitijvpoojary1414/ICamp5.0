def Successor :
  def findSuccessor(self, node) :
    if node is None :
      return 

    if node.right is not None :
      current = node.right 
      while current.left is not None :
        current = current.left 
      return current 
    else :
      firstRightParent = None 
      current = self.root 

      while current is not None :

        if current.val < node.val :
          current = current.right 
        elif current.val > node.val :
          firstRightParent = current
          current = current.left
        else :
          break  

      return firstRightParent

  ## Do range querying
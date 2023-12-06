class LCA :
  def lca(self, a, b) :
    current = self.root 

    while current is not None :
      if a.val < current.val < b.val :
        return current 
      elif a.val > current.val and current.val < b.val :
        current = current.left 
      else :
        current = current.right 

    return -1
    
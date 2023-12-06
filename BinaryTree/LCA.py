class LCA :

  def lcaWithoutParent(self, root, a, b) :
    if root is None :
      return None 

    if root == a or root == b :
      return root 

    left = self.lcaWithoutParent(root.left,a,b)
    right = self.lcaWithoutParent(root.right, a, b)

    if left is not None and right is not None :
      return root 

    return left if left is not None left else right 
    
  def lcaWithParent(self, root, a, b) :
    aPointer = a
    bPointer = b 

    aDepth = 0
    while aPointer ! = root :
      aDepth += 1 
      aPointer = aPointer.getParent()

    bDepth = 0
    while bPointer != root :
      bDepth += 1
      bPointer = bPointer.getParent

    aPointer, bPointer = a,b 

    if aDepth > bDepth :
      big = aDepth
      bigNode = aPointer
      less = bDepth
      lessNode = bPointer
    else :
      big = bDepth
      bigNode = bPointer
      less = aDepth
      lessNode = aPointer

    diff = big - less

    while diff != 0 :
      diff -= 1
      bigNode = bigNode.getParent()

    while bigNode != lessNode :
      bigNode = bigNode.getParent()
      lessNode = lessNode.getParent() 

    return bigNode

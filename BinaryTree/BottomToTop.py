class BottomToTop :
  def height(self, root) :
    if root is None :
      return -1

    return 1 + max(self.height(root.left), self.height(root.right))

  def isBalanced(self,root) :
    val = self.helper(self, root)
    if val == -2 :
      return False 

    return True 

  def helper(self, root) :
    if root is None :
      return -1

    left = self.isBalanced(root.left)
    right = self.isBalanced(root.right)

    if left == -2 or right == -2 :
      return -2

    if abs(right-left) > 1 :
      return -2 

    return 1 + max(left,right)

  def diameter(self, root) :
  
  def diameterHelper(self, root)
    if root is None :
      return (0,-1)

    mdLeft, hLeft = self.diameter(root.left)
    mdRight, hRight = self.diameter(root.right)

    maximum = max([hleft + hRight + 1, mdLeft, mdRight])

    return (maximum, 1 + max(hLeft,hRight))
    
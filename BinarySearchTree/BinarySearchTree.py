class BinarySearchTree :
  def __init__(self) :
    self.root = None 

  def add(self, value) :
    if self.root is None :
      self.root = TreeNode(node)
      return 

    current = self.root 
    parent = None 

    while current is not None :
      parent = current 
      if current.val > value :
        current = current.left
      else :
        current = current.right 

    if parent.val > value :
      parent.left = TreeNode(value)
    else :
      parent.right = TreeNode(value)

  def search(self, value) :
    current = self.root

    while current is not None :
      if current.val > value :
        current = current.left 
      elif value > current.val :
        current = current.right 
      else :
        return current 

    return -1

  def findParent(self, value) :
    parent = None 
    current = self.root 

    while current is not None :
      parent = current 
      if current.val > value :
        current = current.left
      else :
        current = current.right 

    return parent

  def deleteNode(self, node) :
    parentNode = self.findParent(node)

    if node.left is None and node.right is None :
      self.replaceChild(parentNode, node, None)
    elif node.left is None and node.right is not None :
      self.replaceChild(parentNode, node, node.right)
    elif node.right is None and node.left is not None :
      self.replaceChild(parentNode, node, node.left)
    else :
      successor = node.right
      successorParent = None 

      while successor.left is not None :
        successorParent = successor
        successor = successor.left

      value = successor.val
      self.deleteNode(successor)
      node.val = value

  def replaceChild(self, parent, oldChild, newChild) :
    if parent is None :
      self.root = newChild
    elif parent.left == oldChild :
      parent.left = newChild 
    elif parent.right == oldChild :
      parent.right = oldChild 
      
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
      if self.helper(root) is not None:
          return True 

      return False

  def helper(self, root):
      if root is None :
          return(float('inf'),float('-inf'))

      left = self.helper(root.left)
      right = self.helper(root.right)

      if left is None or right is None :
          return None 

      if left[1] >= root.val or root.val >= right[0] :
          return None
      
      minimum = min(root.val, left[0])
      maximum = max(root.val, right[1])
      return (minimum, maximum)


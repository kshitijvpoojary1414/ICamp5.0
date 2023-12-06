class Traversal :
  def inorder(self, root) :
    if root is None :
      return None 

    self.inorder(root.left)
    print(root.val)
    self.inorder(root.right)

  def postorder(self,root) :
    if root is None :
      return None 

    self.postorder(root.left)
    self.postorder(root.right)
    print(root.val)

  def preorder(self, root) :
    if root is None :
      return None 

    print(root.val)
    self.preorder(root.left)
    self.preorder(root.right)

  def inorderIterative(self, root) :
    stack = [root]
    visited = set()

    while len(stack) > 0 :
      node = stack[-1]
      
      if node.left is not None and node.left not in visited :
        stack.push(node)
      else :
        node = stack.pop()
        visited.add(node)
        print(node.val)

        if node.right is not None :
          stack.push(node.right)
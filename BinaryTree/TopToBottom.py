class TopToBottom :
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.height(root,1)

    def height(self, root, currDepth) :
        if root is None :
            return currDepth-1
        left = self.height(root.left, currDepth + 1 )
        right = self.height(root.right,currDepth + 1)
        return max(left,right)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        self.helper(root, result, "")
        return result 

    def helper(self, root, paths, currentPath) :
        if root.left is None and root.right is None:
            currentPath += str(root.val)
            paths.append(currentPath)
            return 

        currentPath += str(root.val) + '->'

        if root.left is not None :
            self.helper(root.left,paths, currentPath )
        
        if root.right is not None :
            self.helper(root.right, paths, currentPath)

        return 
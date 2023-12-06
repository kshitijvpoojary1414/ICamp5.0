class Reconstruction :
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inOrderMap = {}
        for i in range(len(inorder)) :
            inOrderMap[inorder[i]] = i
        return self.helper(preorder, inorder, inOrderMap, 0, len(preorder)-1, 0, len(inorder)-1)


    
    def helper(self, preorder, inorder, inorderMap, preStart, preEnd, inStart, inEnd):

        if preStart > preEnd or inStart > inEnd :
            return 

        root = preorder[preStart]
        inOrderIndex = inorderMap[root]

        root = TreeNode(root)

        root.left = self.helper(preorder, inorder, inorderMap, preStart + 1, preStart + (inOrderIndex-inStart), inStart, inOrderIndex-1)
        root.right = self.helper(preorder, inorder, inorderMap, preStart + (inOrderIndex-inStart) + 1, preEnd, inOrderIndex + 1, inEnd)

        return root
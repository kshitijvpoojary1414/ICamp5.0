class BalancedBST :
  def construct(self, sortedArray) :
    return self.helper(sortedArray, 0, len(sortedArray)-1)
  def helper(self, sortedArray, start, end) :
    if start > end :
      return 

    mid = start + (end - start)//2 

    root = TreeNode(sortedArray[mid])

    root.left = self.helper(sortedArray, mid + 1, end )
    root.right = self.helper(sortedArray, start, mid - 1 )

    return root 

  def findMedian(self, node) :
    slow, fast = node, node 
    prevPtr = null 
    while fast is not None and fast.next is not None :
      fast = fast.next 
      if fast.next is not None :
        fast = fast.next 
      prevPtr = slow 
      slow = slow.next

    if prevPtr != None :
      prevPtr.next = None 
    return slow

  def constructFromLinkedList(self, head) :
    if head is None :
      return None 

    median = self.findMedian(head)

    root = TreeNode(median.val)

    root.left = self.constructFromLinkedList(head)
    root.right = self.constructFromLinkedList(median.next)

    return root


    root.left = self.constructFromLinkedList()
  def helper(self, head) :
    if head is None :
      return 

    


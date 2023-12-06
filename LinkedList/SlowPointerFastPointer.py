class SlowPointerFastPointer :
  def hasCycle(self, head) :
    if head is None :
        return False 

    fast,slow = head, head 

    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next.next 

        if slow == fast :
            return True 

    return False

  def length(self, head) :
    if head is None :
      return False 

    fast,slow = head, head 

    while fast is not None and fast.next is not None:
      slow = slow.next 
      fast = fast.next.next 

      if slow == fast :
        break 

    count = 1
    slow = slow.next 

    while slow != fast :
      slow = slow.next 
      count += 1

    return count 

    
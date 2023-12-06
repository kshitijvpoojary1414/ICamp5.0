class LinkedList :
  def __init__(self) :
    self.head = None 
    self.tail = None 
  
  def append(self, node) :
    if self.head is None :
      self.head = node 
    else :
      self.tail.next = node 
    self.tail = node 

  def delete(self, node, prev) :
    if prev is None :
      self.head = node.next 
    if prev == self.tail :
      self.tail = prev 
    if prev is not None :
      prev.next = None 
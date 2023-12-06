class LinkedHashTable :
  def __init__(self, capacity) :
    self.capacity = capacity 
    self.size = 0
    self.map = {}
    self.head = Node(None) 
    self.tail = Node(None)
    self.head.next = self.tail 
    self.tail.prev = self.head 

  def add(self, key, value) :
    if self.capacity == self.size :
      return 'Full'

    if key in self.map :
      self.update(key, value)
    else :
      node = Node(value)
      self.map[key] = node 
      self.appendToLinkedList(node)

  def remove(self, key, value) :
    if key not in self.map :
      return -1 

    node = self.map[key]
    self.deleteFromLinkedList(node)
    del self.map[key]

  def update(self, key, value) :
    self.remove(key)
    self.add(key, value)
    

  def appendToLinkedList(self, node) :
    nextNode = self.head.next
    self.head.next = node 
    node.prev = self.head
    node.next = nextNode
    nextNode.prev = node 

  def removeFromLinkedList(self, node) :
    prev,nextNode = node.prev,node.next 

    prev.next = node.next 
    nextNode.prev = prev 

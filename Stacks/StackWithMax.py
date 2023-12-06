class StackWithMax :
  def __init__(self, num) :
    self.stack = []
    self.max = [] 

  def push(self, value) :
    self.stack.append(value)

    if len(self.max) == 0 or self.max[-1] <= value :
      self.max.append(value)

  def remove(self, value) :
    if len(self.stack) == 0 :
      return "Empty"

    val = self.stack.pop() 

    if val == self.max[-1] :
      self.max.pop()

    return val 
  
  def max(self) :
    if len(self.max) > 0 :
      return self.max[-1]
    return "Empty"
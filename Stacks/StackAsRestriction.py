# Queue using two stacks
class Queue :
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, num):
        self.s1.push(num)

    def dequeue(self):
        if len(self.s2) == 0 :
            while len(self.s1) > 0:
                self.s2.append(self.s1.pop())

        if len(self.s2) == 0 :
            return None

        return self.s1.pop()

class ArrayStack :
  def __init__(self, num) :
    self.arr = [None]*num
    self.s1 = 0
    self.s2 = num-1

  def add(self, stackNumber, value) :
    if 1 > stackNumber > 2 :
      return False 

    if self.s1 > self.s2 :
      return "Stack is Full"

    if stackNumber == 1 :
      self.arr[self.s1] = value 
      self.s1 += 1
    else :
      self.arr[self.s2] = value 
      self.s2 -= 1

  def remove(self, stackNumber) :
    if 1 > stackNumber > 2 :
      return False 

    if self.s1 > self.s2 :
      return "Stack is Full"

    if stackNumber == 1 and s1 >= 0:
      self.s1 -= 1
    elif stackNumber == 2 and s2 <= len(arr) -1 :
      self.arr[self.s2] = value 
      self.s2 += 1


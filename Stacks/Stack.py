class Stack :
  def contains(self, stack, num) :
    if stack is None :
      return False 

    temp = [] 

    while len(stack) > 0 :
      if (stack[-1] == num) :
        return True 

      temp.append(stack.pop())

    while len(temp) > 0 :
      stack.append(temp.pop())

    return False 
class ExpressionEvaluation :
  def evaluate(self,expression) :
    if len(expression) == 0 :
      return 0

    operator = []
    operand = [] 

    for char in expression :
      if char.isdigit() :
        operand.append(char)
      elif char in ('+','-','*','/') :
        while len(operator) > 0 and self.precedence(char) <= self.precedence(operator[-1]) :
          self.process(operator, operand)
        operator.append(char)
      elif char == "(" :
        operator.append(char)
      elif char == ")" :
    while len(operator) != 0 :
      self.process(operator, operand)

    return operand[-1]

  def process(self, operator, operand) :
    operand2 = operand.pop()
    operand1 = operand.pop()
    operatorVal = operator.pop()

    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "/":
        result = operand1 / operand2
    elif operator == "*":
        result = operand1 * operand2

    operand.push(result)

    return


  def precedence(self, operator):
      if operator == "+":
          return 0
      elif operator == "-":
          return 0
      elif operator == "/":
          return 2
      elif operator == "*":
          return 1
      else:
          raise Exception("")


    

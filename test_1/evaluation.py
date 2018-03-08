class Empty:
    pass

class ArrayStack:
  def __init__(self):
    self.array = []

  def __len__(self):
    return len(self.array)

  def is_empty(self):
    return len(self.array) == 0

  def push(self, e):
    self.array.append(e)

  def top(self):
    if self.is_empty():
      raise Empty()
    return self.array[-1]

  def pop(self):
    if self.is_empty():
      raise Empty()
    return self.array.pop(-1)

  def __repr__(self):
      return str(self.array)
    

def evaluate(string):
    operator_stack = ArrayStack()
    operand_stack = ArrayStack()
    table = {"+":2, "-":2, "*":3, "/":3, "(":1, ")":1}
    pass

print(evaluate("9 + 8 * ( 7 - 6 ) / ( 2 / 8 )"))  #41
print(evaluate("9 + 8 * 7 / ( 6 + 5 ) - ( 4 + 3 ) * 2"))  # 0.0909090909
print(evaluate("9 + 8 * 7 / ( ( 6 + 5 ) - ( 4 + 3 ) * 2 )")) # -9.66666666667
 

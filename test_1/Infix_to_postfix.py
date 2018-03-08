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


def infix_to_postfix(string):
    stack = ArrayStack()
    inputs = string.split(" ")
    precedence = {"+":1, "-":1, "*":2, "/":2, "(":0, ")":0}
    pass


  

infix_to_postfix("( 3 + 2 ) / 4 + ( 3 * 2 + 4 )")
infix_to_postfix("X + Y / ( 5 * Z ) + 10")
            
                    

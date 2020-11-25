from node import *

class Interpreter:
  def __init__(self):
    pass
  def interpret(self, node):
    if type(node) == NumberNode:
      return node.num
    elif type(node) == PlusNode:
      num1 = self.interpret(node.num1)
      num2 = self.interpret(node.num2)
      return num1 + num2
    elif type(node) == MinusNode:
      num1 = self.interpret(node.num1)
      num2 = self.interpret(node.num2)
      return num1 - num2
    elif type(node) == MulNode:
      num1 = self.interpret(node.num1)
      num2 = self.interpret(node.num2)
      return num1 * num2
    elif type(node) == DivNode:
      num1 = self.interpret(node.num1)
      num2 = self.interpret(node.num2)
      return num1 / num2
    elif type(node) == ModNode:
      num1 = self.interpret(node.num1)
      num2 = self.interpret(node.num2)
      return num1 % num2
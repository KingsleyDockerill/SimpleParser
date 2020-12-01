from node import *
from error import *

class Interpreter:
  def __init__(self):
    pass
  def interpret(self, node):
    if type(node) == NumberNode:
      return node.num
    elif type(node) == StringNode:
      return node.string
    elif type(node) == ModNode:
      num1 = self.interpret(node.num1)
      num2 = self.interpret(node.num2)
      return num1 % num2
    elif type(node) == MulNode:
      num1 = self.interpret(node.num1)
      num2 = self.interpret(node.num2)
      return num1 * num2
    elif type(node) == DivNode:
      num1 = self.interpret(node.num1)
      num2 = self.interpret(node.num2)
      return num1 / num2
    elif type(node) == PlusNode:
      num1 = self.interpret(node.num1)
      num2 = self.interpret(node.num2)
      return num1 + num2
    elif type(node) == MinusNode:
      num1 = self.interpret(node.num1)
      num2 = self.interpret(node.num2)
      return num1 - num2
    elif type(node) == PrintNode:
      to_print = []
      for i in node.args:
        to_print.append(str(self.interpret(i)))
      print(" ".join(to_print))
      return None
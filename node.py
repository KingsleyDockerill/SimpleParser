from dataclasses import dataclass

@dataclass
class NumberNode:
  num: float

@dataclass
class PlusNode:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
  def __repr__(self):
    return f"({self.num1}+{self.num2})"

@dataclass
class MinusNode:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
  def __repr__(self):
    return f"({self.num1}-{self.num2})"

@dataclass
class MulNode:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
  def __repr__(self):
    return f"({self.num1}*{self.num2})"

@dataclass
class DivNode:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
  def __repr__(self):
    return f"({self.num1}/{self.num2})"

@dataclass
class ModNode:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2
  def __repr__(self):
    return f"({self.num1}%{self.num2})"
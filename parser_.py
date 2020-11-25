from node import *
from tokens.token import TokenTypes

class Parser:
  def __init__(self, toks):
    self.toks = iter(toks)
    self.tok  = None
    self.advance()
  def advance(self):
    try:
      self.tok = next(self.toks)
    except StopIteration:
      self.tok = None
  def expr(self):
    a = self.muldiv()
    if self.tok != None and self.tok.type_ == TokenTypes.plus:
      self.advance()
      return PlusNode(a, self.expr())
    elif self.tok != None and self.tok.type_ == TokenTypes.minus:
      self.advance()
      return MinusNode(a, self.expr())
    return a
  def muldiv(self):
    a = self.factor()
    self.advance()
    if self.tok != None and self.tok.type_ == TokenTypes.mul:
      self.advance()
      return MulNode(a, self.expr())
    elif self.tok != None and self.tok.type_ == TokenTypes.div:
      self.advance()
      return DivNode(a, self.expr())
    return a 
  def factor(self):
    return NumberNode(self.tok.value)
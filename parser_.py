from node import *
from tokens.token import TokenTypes
from error import*

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
  def lparen_missing(self):
    raise Exception(Error("Syntax Error", f"Missing ( for {self.tok.value}"))
  def argument_divider(self):
    raise Exception(Error("Syntax Error", f"Missing divider , between arguments of {self.tok.value}"))
  def builtins(self):
    if self.tok.type_ != TokenTypes.word:
      a = self.expr()
    if self.tok != None and self.tok.type_ == TokenTypes.word:
      if self.tok.value.lower() == "print":
        self.advance()
        if self.tok.type_ != TokenTypes.lparen:
          self.lparen_missing()
        self.advance()
        args = []
        while self.tok != None and self.tok.type_ != TokenTypes.rparen:
          args.append(self.builtins())
          if self.tok.type_ not in (TokenTypes.comma, TokenTypes.rparen):
            self.argument_divider()
          if self.tok.type_ == TokenTypes.comma:
            self.advance()
        if self.tok is None:
          raise Exception(Error("Early EOF Error", "Expected ) to end arguments, got EOF"))
        self.advance()
        return PrintNode(args)
    try:
      return a
    except:
      pass
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
    a = self.mod()
    self.advance()
    if self.tok != None and self.tok.type_ == TokenTypes.mul:
      self.advance()
      return MulNode(a, self.expr())
    elif self.tok != None and self.tok.type_ == TokenTypes.div:
      self.advance()
      return DivNode(a, self.expr())
    return a
  def mod(self):
    a = self.factor()
    if self.tok != None and self.tok.type_ == TokenTypes.mod:
      self.advance()
      return ModNode(a, self.expr())
    return a
  def factor(self):
    if self.tok.type_ == TokenTypes.float_:
      return NumberNode(self.tok.value)
    elif self.tok.type_ == TokenTypes.string:
      return StringNode(self.tok.value)
    else:
      raise Exception(Error("Syntax Error", """Unexpected token found while parsing"""))
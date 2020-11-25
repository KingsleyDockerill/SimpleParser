from token import TokenTypes, Token
from string import digits

class Lexer:
  def __init__(self, text):
    self.text = iter(text)
    self.char = None
  def advance(self):
    self.char = next(self.text)
  def generate_tokens(self):
    if self.char in " \t\n":
      self.advance()
    elif self.char in digits:
      self.advance()
      yield Token(TokenTypes.float_, self.generate_num())
    elif self.char == "+":
      self.advance()
      yield Token(TokenTypes.plus)
    elif self.char == "-":
      self.advance()
      yield Token(TokenTypes.minus)
    elif self.char == "*":
      self.advance()
      yield Token(TokenTypes.mul)
    elif self.char == "/":
      self.advance()
      yield Token(TokenTypes.div)
    else:
      raise Exception("Illegal token")
  def generate_num(self):
    while self.tok:
      pass
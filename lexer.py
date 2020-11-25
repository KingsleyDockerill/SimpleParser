from tokens.token import TokenTypes, Token
from string import digits

class Lexer:
  def __init__(self, text):
    self.text = iter(text)
    self.char = None
    self.advance()
  def advance(self):
    try:
      self.char = next(self.text)
    except StopIteration:
      self.char = None
  def generate_tokens(self):
    while self.char is not None:
      if self.char in " \t\n":
        self.advance()
      elif self.char in digits:
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
      elif self.char == "%":
        self.advance()
        yield Token(TokenTypes.mod)
      else:
        raise Exception("Illegal token")
  def generate_num(self):
    num = ""
    point_count = 0
    while self.char != None and self.char in digits + ".":
      if point_count > 1:
        raise Exception("Number cannot have more than one .")
      num += self.char
      self.advance()
      if self.char == ".":
        point_count += 1
    return float(num)
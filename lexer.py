from tokens.token import TokenTypes, Token
from string import digits
from error import *

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
      elif self.char == ",":
        self.advance()
        yield Token(TokenTypes.comma)
      elif self.char in "'\"":
        yield Token(TokenTypes.string, self.generate_string(self.char))
      elif self.char == "(":
        yield Token(TokenTypes.lparen)
        self.advance()
      elif self.char == ")":
        yield Token(TokenTypes.rparen)
        self.advance()
      else:
        yield Token(TokenTypes.word, self.generate_word())
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
  def generate_word(self):
    word = ""
    while self.char != None and self.char not in "\n[(":
      word += self.char
      self.advance()
    return word
  def generate_string(self, symbol=""):
    self.advance()
    string = ""
    while self.char not in (None, symbol):
      string += self.char
      self.advance()
    if self.char == None:
      raise Exception(Error("Early EOF Error", "Expected end of string, got EOF"))
    self.advance()
    return string
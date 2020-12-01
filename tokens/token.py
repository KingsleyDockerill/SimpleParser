from enum import Enum
from dataclasses import dataclass

class TokenTypes(Enum):
  float_ = 0
  plus = 1
  minus = 2
  mul = 3
  div = 4
  mod = 5
  word = 6
  string = 7
  lparen = 8
  rparen = 9
  comma = 10
@dataclass
class Token:
  type_: TokenTypes
  value: int = None
  def __repr__(self):
    return f"{self.type_}:{self.value}"
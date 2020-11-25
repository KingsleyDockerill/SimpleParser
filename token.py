from enum import Enum
from dataclasses import dataclass

class TokenTypes(Enum):
  float_ = 0
  plus = 1
  minus = 2
  mul = 3
  div = 4
class Token(dataclass):
  type_: TokenTypes
  value: int = None
  def __repr__(self):
    return f"{self.type_}:" + str(self.value) if self.value != None else "\b"
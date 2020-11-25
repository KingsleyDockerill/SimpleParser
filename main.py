from lexer import Lexer
from parser_ import Parser

while True:
  text = input("> ")
  try:
    lexer = Lexer(text)
    tokens = list(lexer.generate_tokens())
    parser = Parser(tokens)
    nodes = parser.expr()
    print(nodes)
  except Exception as e:
    print(e)
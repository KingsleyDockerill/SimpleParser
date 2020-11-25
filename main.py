from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
  text = input("> ")
  try:
    lexer = Lexer(text)
    tokens = list(lexer.generate_tokens())
    parser = Parser(tokens)
    node = parser.expr()
    interpreter = Interpreter()
    result = interpreter.interpret(node)
    print(result)
  except Exception as e:
    print(e)
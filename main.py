from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
  text = input("> ")
  try:
    lexer = Lexer(text)
    tokens = list(lexer.generate_tokens())
    # print(tokens)
    parser = Parser(tokens)
    node = parser.builtins()
    interpreter = Interpreter()
    result = interpreter.interpret(node)
  except Exception as e:
    print(e)
from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
    try:
        text = input("Kikokotoo v1 > ")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree: continue       #if user doesn't type anything, ignore
        interpreter = Interpreter()
        value = interpreter.visit()
        print(value)
    except Exception as e:
        print(e)
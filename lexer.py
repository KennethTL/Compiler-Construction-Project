from tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '0123456789'

class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):                      # Generates multiple tokens
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_number()        # Yield is used since we are generating numbers
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)
            else:
                raise Exception(f"Illegal Character '{self.current_char}'")
    
    def generate_number(self):
        decimal_point_count = 0
        number_str = self.current_char
        self.advance()

        while self.current_char != None and (self.current_char == "." or self.current_char in DIGITS):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break                           # End of token
                
            number_str += self.current_char
            self.advance()                          # Go to the next char since the entire str is constructed

        if number_str.startswith('.'):
            number_str = '0' + number_str

        if number_str.endswith('.'):
            number_str += '0'

        return Token(TokenType.NUMBER, float(number_str))
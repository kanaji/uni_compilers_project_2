import re


class Calculator:

    def __init__(self):
        self.line: str = ''
        self.current: str = ''

    def parse(self, expr: str) -> float:
        self.line = expr
        result = self.expression()
        if self.line != '':
            raise SyntaxError(f"Unexpected character after expression: '{self.line[0]}'")
        return result

    def expression(self) -> float:  # exp ::= term [ [ '+' | '-' ] term ]*
        result = self.term()
        while self.is_next('[-+]'):
            if self.current == '+':
                result += self.term()
            else:
                result -= self.term()
        return result

    def term(self) -> float:  # term ::= factor [ [ '/' | '*' ] factor ]*
        result = self.factor()
        while self.is_next('[*/]'):
            if self.current == '*':
                result *= self.factor()
            else:
                try:
                    result /= self.factor()
                except ZeroDivisionError:
                    result = float('NaN')  # "Not a Number"
        return result

    def factor(self) -> float:  # factor ::= <number> | '(' exp ')' | '-' factor
        if self.is_next(r'[0-9]*\.?[0-9]+'):
            return float(self.current) if '.' in self.current else int(self.current)
        if self.is_next('-'):
            return -self.factor()
        if self.is_next('[(]'):
            result = self.expression()
            if not self.is_next('[)]'):
                raise SyntaxError(
                    f"Expected ')' but got '{'<EOL>' if not self.line else self.line[0]}'")
            return result
        raise SyntaxError(
            f"Expected number or '-' or '(' but got '{'<EOL>' if not self.line else self.line[0]}'")

    def is_next(self, regexp: str) -> bool:
        m = re.match(r'\s*' + regexp + r'\s*', self.line)
        if m:
            self.current = m.group().strip()
            self.line = self.line[m.end():]
            return True
        return False

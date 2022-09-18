from calc import Calculator


def repl():
    calc = Calculator()
    while True:
        line = input('> ')
        try:
            print(calc.parse(line))
        except SyntaxError as e:
            print(f'Syntax Error: {e.msg}')


if __name__ == '__main__':
    repl()

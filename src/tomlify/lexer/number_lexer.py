from tomlify.lexer.base_lexer import BaseLexer
from tomlify.lexer.token import Literal
from tomlify.lexer.token_type import TokenType


class NumberLexer(BaseLexer):
    def lex(self) -> tuple[int, int]:

        is_integer = True
        is_hex_base = False
        alternate_bases: dict[str, int] = {'b': 2, 'o': 8, 'x': 16}
        base_str: str | None = None

        print("In NumberLexer.lex()")
        print("String =", self._source)
        print("Current is", self._current)
        print("Start is", self._start)
        print("Line is", self._line)

        num = 0
        while True:
            if num > 20:
                break
            num += 1

            # Found base
            if self._peek() == '0' and self._current == self._start:
                print(f"Found starting zero '{self._peek()}'")
                if self._peek(1) in alternate_bases:
                    print(f"Found base '{self._peek(1)}'")
                    base_str = self._peek(1)
                    print(base_str)
                    if base_str == 'x':
                        is_hex_base = True
                    self._advance(2)
                    continue
                self._advance()
                continue

            # Found decimal point
            if self._peek() == '.':
                print("Found decimal point")
                is_integer = False
                if not self._peek(1).isdigit():
                    raise ValueError("Invalid floating point input")
                print(self._current)
                print(self._peek(-1))
                print(self._peek(-1).isdigit())
                if self._peek(-1) == '\0' or not self._peek(-1).isdigit():
                    raise ValueError("Invalid floating point input")
                self._advance(2)
                continue

            # Found exponent
            if not is_integer and self._peek().lower() == 'e':
                print("Found exponent")
                if self._peek(1) == '+' or self._peek(1) == '-':
                    print("Found signed exponent")
                    self._advance(2)
                continue

            # Found hex digit
            if is_hex_base and self._peek() in 'abcdefABCDEF0123456789':
                print(f"Found hex digit '{self._peek()}'")
                self._advance()
                continue

            # Found digit
            if self._peek().isdigit():
                print(f"Found digit '{self._peek()}'")
                self._advance()
                continue

            # Found underscore
            if self._peek() == '_':
                print("Found underscore")
                self._advance()
                continue

            if self._isAtEOF() or self._peek().isspace():
                print("Found whitespace")
                break

            raise ValueError("Invalid number input")

        print("Broken out of loop")
        number_literal = self._source[self._start:self._current]
        print(base_str)
        base: int = 10 if base_str is None else alternate_bases[base_str]
        literal: Literal = int(number_literal, base) if is_integer else float(number_literal)

        self._addToken(TokenType.NUMBER, literal)
        return (self._current, self._line)

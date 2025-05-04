from typing import TYPE_CHECKING

from tomlify.lexer.base_lexer import BaseLexer
from tomlify.lexer.token_type import TokenType

if TYPE_CHECKING:
    from tomlify.lexer.token import Literal


class BinaryLexer(BaseLexer):

    def lex(self) -> tuple[int, int]:
        self._advance(2)

        while True:
            c = self._peek()

            if self._isAtEOF() or self._peek().isspace():
                break

            if c in "01_":
                self._advance()
                continue
            msg = f"Invalid character '{c}' in binary literal."
            raise ValueError(msg)

        literal = int(self._source[self._start:self._current], 2)
        self._add_token(TokenType.NUMBER, literal)
        return (self._current, self._current_line - self._start_line)


class OctalLexer(BaseLexer):
    def lex(self) -> tuple[int, int]:
        self._advance(2)

        while True:
            c = self._peek()

            if self._isAtEOF() or self._peek().isspace():
                break

            if c in "01234567_":
                self._advance()
                continue
            msg = f"Invalid character '{c}' in octal literal."
            raise ValueError(msg)

        literal = int(self._source[self._start:self._current], 8)
        self._add_token(TokenType.NUMBER, literal)
        return (self._current, self._current_line - self._start_line)

class HexLexer(BaseLexer):
    def lex(self) -> tuple[int, int]:
        self._advance(2)

        while True:
            c = self._peek()

            if self._isAtEOF() or self._peek().isspace():
                break

            if c in "abcdefABCDEF0123456789_":
                self._advance()
                continue
            msg = f"Invalid character '{c}' in hexadecimal literal."
            raise ValueError(msg)

        literal = int(self._source[self._start:self._current], 16)
        self._add_token(TokenType.NUMBER, literal)
        return (self._current, self._current_line - self._start_line)


class DecimalLexer(BaseLexer):
    def lex(self) -> tuple[int, int]:

        is_integer = True

        while True:
            c = self._peek()

            if self._isAtEOF() or self._peek().isspace():
                break

            if c == ".":
                is_integer = False
                if not (self._has_leading_digit() and self._has_trailing_digit()):
                    msg = "Invalid floating point input"
                    raise ValueError(msg)
                self._advance()
                continue

            if c in "0123456789_":
                self._advance()
                continue

            if c == "e":
                if is_integer:
                    msg = "Invalid floating point input"
                    raise ValueError(msg)
                self._advance()
                continue

            msg = f"Invalid character '{c}' in decimal literal."
            raise ValueError(msg)

        number_literal = self._source[self._start:self._current]
        literal: Literal = int(number_literal) if is_integer else float(number_literal)
        self._add_token(TokenType.NUMBER, literal)
        return (self._current, self._current_line - self._start_line)

    def _has_leading_digit(self) -> bool:
        return self._peek(1).isdigit()

    def _has_trailing_digit(self) -> bool:
        return self._peek(-1).isdigit()

class NumberLexer(BaseLexer):
    def lex(self) -> tuple[int, int]:

        prefix = self._peek() + self._peek(1)

        match prefix:
            case "0x":
                return self.call_sublexer(HexLexer)
            case "0o":
                return self.call_sublexer(OctalLexer)
            case "0b":
                return self.call_sublexer(BinaryLexer)
            case _:
               return self.call_sublexer(DecimalLexer)

# TODO: Convert to custom exceptions for more detailed info
# TODO: Implement time and date types as tokens
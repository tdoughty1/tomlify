from tomlify.lexer.token import Literal, Token
from tomlify.lexer.token_type import TokenType

class BaseLexer:

    def __init__(self, source: str, start_line: int = 1) -> None:
        self._source: str = source
        self._tokens: list[Token] = []
        self._start: int = 0
        self._current: int = 0
        self._line: int = 1
        self._offset: int = start_line

    def lex(self) -> tuple[int, int]:
        raise NotImplementedError("Subclasses must implement this method")

    def _match(self, expected: str) -> bool:
        if self._isAtEOF():
            return False
        if self._source[self._current] != expected:
            return False
        self._current += 1
        return True

    def _isAtEOF(self, num: int = 0) -> bool:
        return self._current + num >= len(self._source)
    
    def _isAtEOL(self, num: int = 0) -> bool:
        return self._source[self._current + num] == '\n'

    def _advance(self, num: int = 1) -> None:
        if self._isAtEOF():
            raise ValueError("Attempting to advance past end of file.")
        self._current += num

    def _peek(self, num: int = 0) -> str:
        if  self._current + num < 0:
            return '\0'
        if self._isAtEOF() or self._current + num >= len(self._source):
            return '\0'
        return self._source[self._current + num]

    def _addToken(self, type_: TokenType, literal: Literal | None = None) -> None:
        text = self._source[self._start:self._current]
        print(f"Adding token {type_} with text '{text}'")
        print(self._offset)
        current_line = self._offset
        self._tokens.append(Token(type_, text, literal, current_line))

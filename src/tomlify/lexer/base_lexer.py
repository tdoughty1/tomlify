from __future__ import annotations

from abc import ABC, abstractmethod

from tomlify.lexer.token import Literal, Token
from tomlify.lexer.token_type import TokenType


class BaseLexer(ABC):

    def __init__(self, source: str) -> tuple[int, int]:
        self._source: str = source
        self._tokens: list[Token] = []
        self._start: int = 0
        self._current: int = 0
        self._start_line: int = 1
        self._current_line: int = 1


    def call_sublexer(self, sublexer: BaseLexer, delimiter: str | None = None) -> tuple[int]:

        print(f"Calling sublexer {sublexer}")
        lexer = sublexer(self._source[self._current:])

        print("Current line is", self._current_line)
        if delimiter is not None:
            n_chars, n_lines = lexer.lex(delimiter)
        else:
            n_chars, n_lines = lexer.lex()

        print(f"Sublexer returned {n_chars} characters and {n_lines} lines")

        print("Current line is", self._current_line)

        self._current += n_chars
        self._current_line += n_lines
        print(lexer.get_tokens())
        self._tokens.extend(lexer.get_tokens())
        print(self._tokens)
        return (n_chars, self._current_line - self._start_line)

    @abstractmethod
    def lex(self) -> tuple[int, int]:
        pass

    def get_tokens(self) -> list[Token]:
        return self._tokens

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
        self._tokens.append(Token(type_, text, literal, self._start_line))

from tomlify.lexer.base_lexer import BaseLexer
from tomlify.lexer.token_type import TokenType


class StringLexer(BaseLexer):

    def lex(self, delimiter: str = '"') -> tuple[int, int]:
        self._advance()
        while True:

            # Check we haven't gotten to the end of the file or line
            if self._isAtEOF() or self._isAtEOL():
                raise ValueError("Unterminated string.")

            # Check for escaped character
            if self._peek() == '\\':
                self._advance(2)
                continue

            if self._peek() == delimiter:
                break

            self._advance()

        self._advance()
        value = self._source[self._start+1: self._current-1]
        self._addToken(TokenType.STRING, value)
        return (self._current, self._current_line - self._start_line)


class MultilineStringLexer(BaseLexer):

    def lex(self, delimiter: str = '"') -> tuple[int, int]:

        self._advance(3)
        while True:

            print("Current is", self._current)
            print(f"Char is now '{self._peek()}'")

            # Check we haven't gotten to the end of the file or line
            if self._isAtEOF():
                raise ValueError("Unterminated string.")

            # Check for escaped character
            if self._peek() == '\\':
                print("Found escaped character")
                self._advance(2)
                continue

            if self._peek() == delimiter and self._peek(1) == delimiter and self._peek(2) == delimiter:
                print("Found ending delimiter")
                break

            if self._peek() == '\n':
                print("Found new line")
                self._current_line += 1

            self._advance()

        self._advance(3)
        print("String is", self._source[self._start: self._current])
        value = self._source[self._start + 3: self._current - 3]
        self._addToken(TokenType.STRING, value)
        print("Tokens are", self._tokens)
        print("Offset is", self._current - self._start)
        return (self._current, self._current_line - self._start_line)


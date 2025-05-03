from abc import ABC

from tomlify.lexer import Lexer
from tomlify.lexer.token_type import TokenType

class StringScanner(Lexer):

    def scanString(self, delimiter: str = '"'):
        while True:
            
            if self._peek() == delimiter:
                print("Found end of string")
                break

            # Check we haven't gotten to the end of the file or line
            if self._isAtEOF() or self._isAtEOL():
                raise ValueError(self._line, "Unterminated string.")

            # Ignore escaped characters
            if self._peek() == '\\':
                if self._peek(1) == 'n':
                    raise ValueError("Newlines are not allowed in basic strings.")
                self._advance()

            print("Found standard character")
            self._advance()
            print(f"Current is {self._current}")
            print(f"Start is {self._start}")
            value = self._source[self._start + 1: self._current - 1]
            print(f"Found string '{value}'")
            self._addToken(TokenType.STRING, value)
            # The closing ".


class MultilineStringScanner(Lexer):

    def scanString(self, delimiter: str = '"'):
        while True:
            if self._peek() == delimiter:
                print("Found end of string")
                break

            # Check we haven't gotten to the end of the file or line
            if self._isAtEOF() or self._isAtEOL():
                raise ValueError(self._line, "Unterminated string.")

            # Ignore escaped characters
            if self._peek() == '\\':
                print("Found escape character")
                if self._peek(1) == 'n' and not is_multiline:
                    raise ValueError("Newlines are not allowed in basic strings.")
                self._advance()

            if self._isAtEOL():
                print("Found end of line")
                if is_multiline:
                    print("Found end of line in multiline string")
                    self._start_line = self._line + 1
                    self._current_line = self._start_line
                    break
                else:
                    print("Found end of line in basic string")
                    raise ValueError("Unterminated basic string.")
                
            print("Found standard character")
            self._advance()



        # Closing the string
        if is_multiline:
            # The closing ".
            self._advance(3)
            print(f"Current is {self._current}")
            print(f"Start is {self._start}")
            value = self._source[self._start + 3: self._current - 3]
            self._addToken(TokenType.STRING, value)

        else:
            self._advance()
            value = self._source[self._start + 1: self._current - 1]
            self._addToken(TokenType.STRING, value)


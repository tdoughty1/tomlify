from __future__ import annotations

from tomlify.lexer.base_lexer import BaseLexer
from tomlify.lexer.token import Token
from tomlify.lexer.token_type import TokenType


class Lexer(BaseLexer):

    def __init__(self, source: str) -> None:
        self._source: str = source
        self._tokens: list[str] = []
        self._start: int = 0
        self._current: int = 0
        self._line: int = 1

    
    def lexTokens(self) -> list[Token]:
        """Tokenizes the source text for relevent TOML lexemes

        This method starts at the beginning of the next lexeme and
        continues until the end of the file is reached. Once all
        tokens have been scanned, an EOF token is appended to the
        tokens list.

        Returns:
            list[Token]: The list of tokens found in the source text.
        """
        while not self._isAtEOF():
            # We are at the beginning of the next lexeme.
            self._start = self._current
            self._lexToken()
        
        self._tokens.append(Token(TokenType.EOF, "", None, self._line))
        return self._tokens
 
    def _lexToken(self) -> None:
        c = self._peek()
        self._advance()
        print(f"Start is {self._start}, Current is {self._current}, Char is '{c}'")
        match c:
            case '#':
                self._comment()
                return
            case '"' | "'":
                self._string(delimiter = c)
                return
            case '.':
                self._addToken(TokenType.DOT)
                return
            case '{':
                self._addToken(TokenType.LEFT_BRACE)
                return
            case '}':
                self._addToken(TokenType.RIGHT_BRACE)
                return
            case ':':
                self._addToken(TokenType.COLON)
                return
            case '=':
                self._addToken(TokenType.EQUAL)
                return
            case ',':
                self._addToken(TokenType.COMMA)
                return
            case ' ':
                return
            case '\n'|'\r':
                self._addToken(TokenType.NEWLINE)
                self._line += 1
                return
            case _:
                if c.isdigit():
                    self._number()
                elif c.isalpha():
                    self._identifier()
                else:
                    raise ValueError(f"Unexpected character '{repr(c)}' on line {self._line}")

    
    def _addToken(self, type_: str, literal: str = None) -> None:
        text = self._source[self._start:self._current]
        text = '\n' if text == '\n' else text
        self._tokens.append(Token(type_, text, literal, self._line))

    def _isidentifier(self, c: str) -> bool:
        return c.isalnum() or c == '_' or c == '-'

    def _identifier(self) -> None:
        while (self._isidentifier(self._peek())):
            self._advance()

        self._addToken(TokenType.IDENTIFIER)

    def _number(self) -> None: 
        while self._peek().isdigit():
            self._advance()

        # Look for a fractional part.
        if (self._peek() == '.' and self._peek().isdigit()):
            # Consume the "."
            self._advance()
            while (self._peek().isdigit()):
                self._advance()

        self._addToken(TokenType.NUMBER, float(self._source[self._start:self._current]))


    def _comment(self) -> None:
        # A comment goes until the end of the line.
        while (self._peek() != '\n') and not self._isAtEOF():
            self._advance()
        value = self._source[self._start + 1: self._current]
        print(value)
        self._addToken(TokenType.COMMENT, value)
        return


    def _string(self, delimiter: str = '"') -> None:

        print(f"In string for {self._source}, length is {len(self._source)}")
        print(f"Delimiter is {delimiter}")
        print(f"Start is {self._start}")
        print(f"Line is {self._line}")

        is_multiline = False

        while True:
            
            if is_multiline:
                print(f"Line is {self._line}")

            print(f"Start is {self._start}, Current is {self._current}, Char is '{self._source[self._current]}'")

            # Check we haven't gotten to the end of the file or line
            if self._isAtEOF():
                print("At EOF")
                raise ValueError(self._line, "Unterminated string.")

            # Logic for when you find the same delimiter after the start
            if not is_multiline and self._peek() == delimiter and self._peek(1) == delimiter:
                is_multiline = True
                self._advance(2)
                print("Found multiline string")

            if self._peek() == delimiter and not is_multiline:
                print("Found end of string")
                break

            if self._peek() == delimiter and self._peek(1) == delimiter and self._peek(2) and is_multiline:
                print("Found end of multiline string")
                break

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

        if self._isAtEOF():
            raise ValueError("Unterminated string.")

        # Closing the string
        if is_multiline:
            # The closing ".
            self._advance(3)
            print(f"Current is {self._current}")
            print(f"Start is {self._start}")
            value = self._source[self._start + 3: self._current - 3]
            print(f"Found multiline string '{value}'")
            self._addToken(TokenType.STRING, value)

        else:
            self._advance()
            print(f"Current is {self._current}")
            print(f"Start is {self._start}")
            value = self._source[self._start + 1: self._current - 1]
            print(f"Found string '{value}'")
            self._addToken(TokenType.STRING, value)
            # The closing ".

# TODO add support for multiline strings
# TODO add support escape characters for strings
# TODO add support for line starting indent
# TODO add support for underscored numbers
# TODO add support for hyphen in identifiers
# TODO add support for number dotted keys
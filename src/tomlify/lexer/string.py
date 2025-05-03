from abc import ABC
from tomlify.lexer import Lexer

class StringScanner(Lexer):

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

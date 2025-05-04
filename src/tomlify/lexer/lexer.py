from __future__ import annotations

from tomlify.lexer.base_lexer import BaseLexer
from tomlify.lexer.comment_lexer import CommentLexer
from tomlify.lexer.identifier_lexer import IdentifierLexer
from tomlify.lexer.number_lexer import NumberLexer
from tomlify.lexer.string_lexer import MultilineStringLexer, StringLexer
from tomlify.lexer.token import Token
from tomlify.lexer.token_type import TokenType

TOKEN_TYPE_MAP = {
    '.': TokenType.DOT,
    '{': TokenType.LEFT_BRACE,
    '}': TokenType.RIGHT_BRACE,
    '[': TokenType.LEFT_BRACKET,
    ']': TokenType.RIGHT_BRACKET,
    ',': TokenType.COMMA,
    ':': TokenType.COLON,
    '=': TokenType.EQUAL,
    '-': TokenType.MINUS,
    '+': TokenType.PLUS,
    '/': TokenType.SLASH,
}

class Lexer(BaseLexer):

    def lex(self) -> tuple[int, int]:
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

        print(self._current_line)

        self._tokens.append(Token(TokenType.EOF, "", None, self._current_line))
        return self._current, self._current_line - self._start_line

    def _lexToken(self) -> None:
        c = self._peek()
        print(f"Start is {self._start}, Current is {self._current}, Char is '{c}'")
        match c:
            case '#':
                return self.call_sublexer(CommentLexer)
            case '"' | "'":
                print("Current line is", self._current_line)
                if self._peek(1) == c and self._peek(2) == c:
                    print("Current line is", self._current_line)
                    self.call_sublexer(MultilineStringLexer, delimiter=c)
                else:
                    self.call_sublexer(StringLexer, delimiter=c)
            case '.'|'{'|'}'|':'|'='|','|'-'|'+':
                self._advance()
                token = TOKEN_TYPE_MAP[c]
                self._addToken(token)
            case ' ':
                self._advance()
            case '\n'|'\r':
                self._advance()
                self._addToken(TokenType.NEWLINE)
                print("Current line is", self._current_line)
                self._current_line += 1
                print("Current line is", self._current_line)
            case _:
                if c.isdigit():
                    self.call_sublexer(NumberLexer)
                elif c.isalpha():
                    print("Current line is", self._current_line)
                    self.call_sublexer(IdentifierLexer)
                    print("Current line is", self._current_line)
                else:
                    raise ValueError(f"Unexpected character '{c!r}' on line {self._current_line}")
        return None

# TODO add support for line starting indent

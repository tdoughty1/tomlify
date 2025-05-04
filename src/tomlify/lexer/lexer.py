from __future__ import annotations

from tomlify.lexer.base_lexer import BaseLexer
from tomlify.lexer.comment_lexer import CommentLexer
from tomlify.lexer.identifier_lexer import IdentifierLexer
from tomlify.lexer.number_lexer import NumberLexer
from tomlify.lexer.string_lexer import MultilineStringLexer, StringLexer
from tomlify.lexer.token import Token
from tomlify.lexer.token_type import TokenType

TOKEN_TYPE_MAP = {
    ".": TokenType.DOT,
    "{": TokenType.LEFT_BRACE,
    "}": TokenType.RIGHT_BRACE,
    "[": TokenType.LEFT_BRACKET,
    "]": TokenType.RIGHT_BRACKET,
    ",": TokenType.COMMA,
    ":": TokenType.COLON,
    "=": TokenType.EQUAL,
    "-": TokenType.MINUS,
    "+": TokenType.PLUS,
    "/": TokenType.SLASH,
}

class Lexer(BaseLexer):

    def lex(self) -> tuple[int, int]:
        """Tokenizes the source text for relevent TOML lexemes.

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
            self._lextoken()

        self._tokens.append(Token(TokenType.EOF, "", None, self._current_line))
        return self._current, self._current_line - self._start_line

    def _lextoken(self) -> None:
        c = self._peek()
        match c:
            case "#":
                self.call_sublexer(CommentLexer)
            case '"' | "'":
                if self._peek(1) == c and self._peek(2) == c:
                    self.call_sublexer(MultilineStringLexer, delimiter=c)
                else:
                    self.call_sublexer(StringLexer, delimiter=c)
            case "."|"{"|"}"|":"|"="|","|"-"|"+":
                self._advance()
                token = TOKEN_TYPE_MAP[c]
                self._add_token(token)
            case " ":
                self._advance()
            case "\n"|"\r":
                self._advance()
                self._add_token(TokenType.NEWLINE)
                self._current_line += 1
            case _:
                if c.isdigit():
                    self.call_sublexer(NumberLexer)
                elif c.isalpha():
                    self.call_sublexer(IdentifierLexer)
                else:
                    msg = f"Unexpected character '{c!r}' on line {self._current_line}"
                    raise ValueError(msg)

# TODO: add support for line starting indent

from __future__ import annotations

from tomlify.lexer.base_lexer import BaseLexer
from tomlify.lexer.comment_lexer import CommentLexer
from tomlify.lexer.identifier_lexer import IdentifierLexer
from tomlify.lexer.number_lexer import NumberLexer
from tomlify.lexer.string_lexer import MultilineStringLexer, StringLexer
from tomlify.lexer.token import Token
from tomlify.lexer.token_type import TokenType


class Lexer(BaseLexer):

    def lexTokens(self) -> list[Token]:
        """Tokenizes the source text for relevent TOML lexemes

        This method starts at the beginning of the next lexeme and
        continues until the end of the file is reached. Once all
        tokens have been scanned, an EOF token is appended to the
        tokens list.

        Returns:
            list[Token]: The list of tokens found in the source text.

        """
        num = 0
        while not self._isAtEOF():
            if num > 50:
                break
            num += 1
            # We are at the beginning of the next lexeme.
            self._start = self._current
            self._lexToken()

        self._tokens.append(Token(TokenType.EOF, "", None, self._line))
        return self._tokens

    def _lexToken(self) -> None:
        c = self._peek()
        print(f"Start is {self._start}, Current is {self._current}, Char is '{c}'")
        match c:
            case '#':
                lexer: BaseLexer = CommentLexer(self._source[self._current:])
                n_chars, _ = lexer.lex()
                self._current += n_chars
                self._tokens.extend(lexer._tokens)
                return
            case '"' | "'":
                if self._peek(1) == c and self._peek(2) == c:
                    lexer = MultilineStringLexer(self._source[self._current:])
                    n_chars, n_lines = lexer.lex(c)
                    self._current += n_chars
                    self._line += n_lines - 1
                    self._tokens.extend(lexer._tokens)

                    return
                lexer = StringLexer(self._source[self._current:])
                n_chars, _ = lexer.lex(c)
                self._current += n_chars
                self._tokens.extend(lexer._tokens)
                return
            case '.':
                self._advance()
                self._addToken(TokenType.DOT)
                return
            case '{':
                self._advance()
                self._addToken(TokenType.LEFT_BRACE)
                return
            case '}':
                self._advance()
                self._addToken(TokenType.RIGHT_BRACE)
                return
            case ':':
                self._advance()
                self._addToken(TokenType.COLON)
                return
            case '=':
                print("Found equal sign")
                self._advance()
                self._addToken(TokenType.EQUAL)
                return
            case ',':
                self._advance()
                self._addToken(TokenType.COMMA)
                return
            case ' ':
                self._advance()
                return
            case '\n'|'\r':
                self._advance()
                self._addToken(TokenType.NEWLINE)
                self._line += 1
                return
            case _:
                if c.isdigit():
                    lexer = NumberLexer(self._source[self._current:])
                    n_chars, _ = lexer.lex()
                    self._current += n_chars
                    self._tokens.extend(lexer._tokens)
                elif c.isalpha():
                    lexer = IdentifierLexer(self._source[self._current:])
                    n_chars, _ = lexer.lex()
                    self._current += n_chars
                    self._tokens.extend(lexer._tokens)
                else:
                    raise ValueError(f"Unexpected character '{c!r}' on line {self._line}")

# TODO add support for line starting indent

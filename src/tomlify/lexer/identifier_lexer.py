from tomlify.lexer.base_lexer import BaseLexer
from tomlify.lexer.token_type import TokenType


class IdentifierLexer(BaseLexer):
    def lex(self) -> None:
        while (self._isidentifier(self._peek())):
            self._advance()

        self._addToken(TokenType.IDENTIFIER)
        return (self._current, self._line)

    @staticmethod
    def _isidentifier(c: str) -> bool:
        return c.isalnum() or c == '_' or c == '-'

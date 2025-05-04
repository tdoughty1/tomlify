from tomlify.lexer.base_lexer import BaseLexer
from tomlify.lexer.token_type import TokenType


class IdentifierLexer(BaseLexer):
    def lex(self) -> tuple[int, int]:
        while (self._isidentifier(self._peek())):
            self._advance()

        self._add_token(TokenType.IDENTIFIER)
        return (self._current, self._current_line - self._start_line)

    @staticmethod
    def _isidentifier(c: str) -> bool:
        return c.isalnum() or c in {"_", "-"}

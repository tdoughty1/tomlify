from dataclasses import dataclass

from tomlify.lexer.token_type import TokenType

Literal = str | int | float

@dataclass
class Token:
    type_: TokenType
    lexeme: str
    literal: Literal | None
    line: int

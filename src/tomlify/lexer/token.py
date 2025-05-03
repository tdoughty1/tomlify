from dataclasses import dataclass

from tomlify.lexer.token_type import TokenType

@dataclass
class Token():   
    type_: TokenType
    lexeme: str
    literal: str | None
    line: int

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from typing_extensions import Self

if TYPE_CHECKING:
    from tomlify.lexer.lex_token import Literal, Token


class KeyValue:
    def __init__(self, key: Key, value: Token) -> None:
        self.key = key
        self.value = value

    def __repr__(self) -> str:
        return f"KeyValue({self.key.name} = {self.value.literal})"


@dataclass
class Value:
    token: Token
    literal: Literal | None

    def __init__(self, token: Token) -> None:
        self.token = token
        self.literal = token.literal


@dataclass
class Key:

    tokens: list[Token]
    name: Literal | None

    # Initial Call is the construction with a single name
    def __init__(self, token: Token) -> None:
        self.tokens = [token]
        self.name: str = token.lexeme if token.lexeme else str(token.literal)

    # Followup calls return new instances of Key appending them together
    def __iadd__(self, key: Key | None) -> Self:
        if key:
            self.tokens.extend(key.tokens)
            self.name =  f"{self.name}.{key.name}"
        return self

    def __repr__(self) -> str:
        return f"Key({self.name})"


class Array(list[Value], Value):

    def __init__(self, *args: Value) -> None:
        super().__init__(args)


@dataclass
class Table:
    def __init__(self, key: Key) -> None:
        self.key = key


@dataclass
class InlineTable(list[KeyValue], KeyValue):
    def __init__(self, *args: KeyValue) -> None:
        super().__init__(args)


@dataclass
class ArrayTable(Table):
    key: Key


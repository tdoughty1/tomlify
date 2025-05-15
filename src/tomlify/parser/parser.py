
from tomlify.lexer.lex_token import Token
from tomlify.lexer.token_type import TokenType
from tomlify.parser.exceptions import (
    InvalidArrayError,
    InvalidArrayTableError,
    InvalidInlineTableError,
    InvalidTableError,
)
from tomlify.parser.expr import (
    Array,
    ArrayTable,
    InlineTable,
    Key,
    KeyValue,
    Table,
    Value,
)


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self._tokens: list[Token] = tokens
        self._current = 0

    def parse(self) -> list[KeyValue]:
        return self._toml()

    def _advance(self, num: int = 1) -> None:
        self._current += num

    def _retreat(self) -> None:
        self._current -= 1

    def _isAtEnd(self) -> bool: # noqa: N802
        check = self._current >= len(self._tokens)
        return check or self._peek().type_ == TokenType.EOF

    def _peek(self, num: int = 0) -> Token:
        return self._tokens[self._current + num]

    def _previous(self) -> Token:
        return self._tokens[self._current - 1]

    def _match(self, *types: TokenType) -> bool:
        for type_ in types:
            if self._check(type_):
                self._advance()
                return True
        return False

    def _check(self, type_: TokenType) -> bool:
        if self._isAtEnd():
            return False
        return self._peek().type_ == type_

    def _toml(self) -> list[KeyValue]:
        expressions: list[KeyValue] = []
        initial_expression = self._expression()
        if initial_expression:
            expressions.append(initial_expression)
        while self._match(TokenType.NEWLINE) and not self._isAtEnd():
            expression = self._expression()
            if expression:
                expressions.append(expression)
        return expressions

    def _expression(self) -> KeyValue | None:
        if self._match(TokenType.NEWLINE):
            return None
        if self._match(TokenType.COMMENT):
            return None

        return self._key_val()

    def _key_val(self) -> KeyValue | None:
        key = self._key()
        sep = self._key_val_sep()
        value = self._val()
        if key and sep and value:
            return KeyValue(key, value)
        return None

    def _key(self) -> Key | None:
        if (simple_key := self._simple_key()) and (self._peek().type_ != TokenType.DOT):
            return simple_key
        # step back since simple_key consumed one token, but wasn't used if we get here
        self._retreat()
        if dotted_key := self._dotted_key():
            return dotted_key
        return None

    def _dotted_key(self) -> Key | None:
        dotted_key = self._simple_key()
        if not dotted_key:
            return None
        while self._match(TokenType.DOT):
            dotted_key += self._simple_key()
        return dotted_key

    def _simple_key(self) -> Key | None:
        if quoted_key := self._quoted_key():
            return quoted_key
        if unquoted_key := self._unquoted_key():
            return unquoted_key
        return None

    def _quoted_key(self) -> Key | None:
        if self._match(TokenType.STRING):
            return Key(self._previous())
        return None

    def _unquoted_key(self) -> Key | None:
        if self._match(TokenType.IDENTIFIER):
            token = self._previous()
            return Key(token)
        return None

    def _key_val_sep(self) -> Token | None:
        if self._match(TokenType.EQUAL):
            return self._previous()
        return None

    def _val(self) -> Value | None:
        if self._match(TokenType.STRING):
            return Value(self._previous())
        if self._match(TokenType.BOOLEAN):
            return Value(self._previous())
        if self._match(TokenType.DATE):
            self._advance()
            return Value(self._previous())
        if self._match(TokenType.NUMBER):
            self._advance()
            return Value(self._previous())
        if self._match(TokenType.NUMBER):
            self._advance()
            return Value(self._previous())
        raise ValueError

    def _array(self) -> Array | None:  # noqa: C901
        if self._peek().type_ != TokenType.LEFT_BRACKET:
            return None
        self._advance()

        elements = Array()
        while True:
            # Handle nested array
            if self._peek().type_ == TokenType.LEFT_BRACKET:
                array = self._array()
                if array:
                    elements.append(array)
                else:
                    msg = "Invalid Nested Array Formatting"
                    raise InvalidArrayError(msg)
                continue

            # Handles case of trailing comma or newline in array list
            if self._match(TokenType.RIGHT_BRACKET):
                break

            if self._match(TokenType.NEWLINE):
                continue

            if self._match(TokenType.COMMENT):
                continue

            # Handles no trailing comma case in array list
            if self._peek(1).type_ == TokenType.RIGHT_BRACKET:
                elements.append(Value(self._tokens[self._current]))
                self._advance(2)
                break

            if self._peek(1).type_ == TokenType.NEWLINE:
                elements.append(Value(self._tokens[self._current]))
                self._advance(2)
                continue

            if self._peek(1).type_ == TokenType.COMMA:
                elements.append(Value(self._tokens[self._current]))
                self._advance(2)
                continue
            msg = "Invalid Array Formatting"
            raise InvalidArrayError(msg)

        return Array(*elements)

    def _table(self) -> Table | None:
        if std_table := self._std_table():
            return std_table
        if array_table := self._array_table():
            return array_table
        return None


    def _std_table(self) -> Table | None:
        if not self._match(TokenType.LEFT_BRACKET):
            return None
        key = self._key()
        if not key:
            msg = "Invalid Table Name Key"
            raise InvalidTableError(msg)
        if not self._match(TokenType.RIGHT_BRACKET):
            msg = "Invalid Table Formatting"
            raise InvalidTableError(msg)
        return Table(key)

    def _array_table(self) -> ArrayTable | None:
        if not self._match(TokenType.DOUBLE_LEFT_BRACKET):
            return None
        key = self._key()
        if not key:
            msg = "Invalid Array Table Name Key"
            raise InvalidArrayTableError(msg)
        if not self._match(TokenType.DOUBLE_RIGHT_BRACKET):
            msg = "Invalid Array Table Formatting"
            raise InvalidArrayTableError(msg)
        return ArrayTable(key)


    def _inline_table(self) -> InlineTable | None:
        if not self._match(TokenType.LEFT_BRACE):
            return None

        inline_table = InlineTable()

        while True:
            if self._peek().type_ == TokenType.RIGHT_BRACE:
                self._advance()
                return inline_table

            keyval = self._key_val()
            if not keyval:
                msg = "Invalid Inline Table Formatting"
                raise InvalidInlineTableError(msg)
            inline_table.append(keyval)

            if self._match(TokenType.COMMA):
                continue
            if self._peek().type_ == TokenType.RIGHT_BRACE:
                continue
            msg = "Invalid Inline Table Formatting"
            raise InvalidInlineTableError(msg)

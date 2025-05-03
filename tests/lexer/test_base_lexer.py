import pytest

from tomlify.lexer.base_lexer import BaseLexer
from tomlify.lexer.token import Token
from tomlify.lexer.token_type import TokenType

def test_match() -> None:
    lexer = BaseLexer("test")
    assert lexer._match("t")
    assert lexer._match("e")
    assert lexer._match("s")
    assert lexer._match("t")

def test_not_match() -> None:
    lexer = BaseLexer("test")
    assert not lexer._match("a")

def test_match_EOF() -> None:
    lexer = BaseLexer("test")
    assert lexer._match("t")
    assert lexer._match("e")
    assert lexer._match("s")
    assert lexer._match("t")
    assert lexer._isAtEOF()

def test_EOF() -> None:
    lexer = BaseLexer("")
    assert lexer._isAtEOF()

def test_not_EOF() -> None:
    lexer = BaseLexer("test")
    assert not lexer._isAtEOF()

def test_EOF_three_chars() -> None:
    lexer = BaseLexer("abc")
    assert lexer._isAtEOF(3)

def test_not_EOF_two_chars() -> None:
    lexer = BaseLexer("abc")
    assert not lexer._isAtEOF(2)


def test_isAtEOL() -> None:
    lexer = BaseLexer('\n')
    assert lexer._isAtEOL()

def test_not_isAtEOL() -> None:
    lexer = BaseLexer('a')
    assert not lexer._isAtEOL()

def test_isAtEOL_three_chars() -> None:
    lexer = BaseLexer('abc\n')
    assert lexer._isAtEOL(3)

def test_not_isAtEOL_two_chars() -> None:
    lexer = BaseLexer('abc\n')
    assert not lexer._isAtEOL(2)

def test_advance() -> None:
    lexer = BaseLexer("test")
    lexer._advance()
    assert lexer._current == 1

def test_advance_end_of_file() -> None:
    lexer = BaseLexer("")
    with pytest.raises(ValueError):
        lexer._advance()

def test_advance_two_chars() -> None:
    lexer = BaseLexer("test")
    lexer._advance(2)
    assert lexer._current == 2

def test_peek() -> None:
    lexer = BaseLexer("test")
    assert lexer._peek() == 't'
    assert lexer._peek(1) == 'e'
    assert lexer._peek(2) == 's'
    assert lexer._peek(3) == 't'

def test_peek_EOF() -> None:
    lexer = BaseLexer("test")
    assert lexer._peek() == 't'
    assert lexer._peek(1) == 'e'
    assert lexer._peek(2) == 's'
    assert lexer._peek(3) == 't'
    assert lexer._peek(4) == '\0'


def test_no_match() -> None:
    lexer = BaseLexer("a")
    assert not lexer._match("b")


def test_no_match_EOF() -> None:
    lexer = BaseLexer("")
    assert not lexer._match("t")


def test_add_token() -> None:
    lexer = BaseLexer("")
    lexer._addToken(TokenType.IDENTIFIER, "test")
    assert lexer._tokens == [Token(TokenType.IDENTIFIER, "", "test", 1)]    

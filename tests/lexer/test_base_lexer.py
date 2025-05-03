import pytest

from tomlify.lexer.base_lexer import BaseLexer

def test_match():
    lexer = BaseLexer("test")
    assert lexer._match("t")
    assert lexer._match("e")
    assert lexer._match("s")
    assert lexer._match("t")

def test_not_match():
    lexer = BaseLexer("test")
    assert not lexer._match("a")

def test_match_EOF():
    lexer = BaseLexer("test")
    assert lexer._match("t")
    assert lexer._match("e")
    assert lexer._match("s")
    assert lexer._match("t")
    assert lexer._isAtEOF()

def test_EOF():
    lexer = BaseLexer("")
    assert lexer._isAtEOF()

def test_not_EOF():
    lexer = BaseLexer("test")
    assert not lexer._isAtEOF()

def test_EOF_three_chars():
    lexer = BaseLexer("abc")
    assert lexer._isAtEOF(3)

def test_not_EOF_two_chars():
    lexer = BaseLexer("abc")
    assert not lexer._isAtEOF(2)


def test_isAtEOL():
    lexer = BaseLexer('\n')
    assert lexer._isAtEOL()

def test_not_isAtEOL():
    lexer = BaseLexer('a')
    assert not lexer._isAtEOL()

def test_isAtEOL_three_chars():
    lexer = BaseLexer('abc\n')
    assert lexer._isAtEOL(3)

def test_not_isAtEOL_two_chars():
    lexer = BaseLexer('abc\n')
    assert not lexer._isAtEOL(2)

def test_advance():
    lexer = BaseLexer("test")
    lexer._advance()
    assert lexer._current == 1

def test_advance_end_of_file():
    lexer = BaseLexer("")
    with pytest.raises(ValueError):
        lexer._advance()

def test_advance_two_chars():
    lexer = BaseLexer("test")
    lexer._advance(2)
    assert lexer._current == 2

def test_peek():
    lexer = BaseLexer("test")
    assert lexer._peek() == 't'
    assert lexer._peek(1) == 'e'
    assert lexer._peek(2) == 's'
    assert lexer._peek(3) == 't'

def test_peek_EOF():
    lexer = BaseLexer("test")
    assert lexer._peek() == 't'
    assert lexer._peek(1) == 'e'
    assert lexer._peek(2) == 's'
    assert lexer._peek(3) == 't'
    assert lexer._peek(4) == '\0'

def test_match():
    lexer = BaseLexer("a")
    assert lexer._match("a")


def test_no_match():
    lexer = BaseLexer("a")
    assert not lexer._match("b")


def test_match_EOF():
    lexer = BaseLexer("")
    assert not lexer._match("t")
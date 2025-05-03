import pytest

from tomlify.lexer.string_lexer import MultilineStringLexer,StringLexer
from tomlify.lexer.token import Token
from tomlify.lexer.token_type import TokenType

def build_string_token(input_string: str, multiline: bool = False) -> list[Token]:
    if multiline:
        return [Token(TokenType.STRING, input_string, input_string[3:-3], 1)]
    return [Token(TokenType.STRING, input_string, input_string[1:-1], 1)]

def test_lex_string() -> None:
    input_string = '"test"'
    lexer = StringLexer(input_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == build_string_token(input_string)
    assert n_chars == len(input_string)
    assert n_lines == 1

def test_lex_string_with_escaped_quote() -> None:
    input_string = '"I am a \\"test\\" for now"'
    lexer = StringLexer(input_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == build_string_token(input_string)
    assert n_chars == len(input_string)
    assert n_lines == 1

def test_lex_unterminated_string() -> None:
    lexer = StringLexer('"Th')
    with pytest.raises(ValueError):
        lexer.lex()

def test_lex_unterminated_new_line() -> None:
    lexer = StringLexer('"Th\n')
    with pytest.raises(ValueError):
        lexer.lex()

def test_lex_apostrophe_string() -> None:
    input_string = "'test'"
    lexer = StringLexer(input_string)
    n_chars, n_lines = lexer.lex(delimiter="'")
    assert lexer._tokens == build_string_token(input_string)
    assert n_chars == len(input_string)
    assert n_lines == 1

def test_lex_multiline_string() -> None:
    input_string = r'"""This is a string.\n Split over lines."""'
    lexer = MultilineStringLexer(input_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == build_string_token(input_string, True)
    assert n_chars == len(input_string)
    assert n_lines == 2

def test_lex_multiline_unterminated_string() -> None:
    lexer = MultilineStringLexer('"""This is a string.\n Split over lines.')
    with pytest.raises(ValueError):
        lexer.lex()

def test_lex_multiline_apostrophe_string() -> None:
    input_string = "'''This is a string.\n Split over lines.'''"
    lexer = MultilineStringLexer(input_string)
    n_chars, n_lines = lexer.lex(delimiter="'")
    assert lexer._tokens == build_string_token(input_string, True)
    assert n_chars == len(input_string)
    assert n_lines == 2

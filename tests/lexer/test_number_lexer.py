import pytest

from tomlify.lexer.number_lexer import NumberLexer
from tomlify.lexer.token import Token
from tomlify.lexer.token_type import TokenType

def test_number_int() -> None:
    input_num_string = "99"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 99, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 0

def test_number_int_zero() -> None:
    input_num_string = "0"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 0, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 0

def test_number_underscore() -> None:
    input_num_string = "1_000"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 1000, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 0

def test_number_multiple_underscore() -> None:
    input_num_string = "1_2_3_4_5"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 12345, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 0

def test_number_hex_uppercase() -> None:
    input_num_string = "0xDEADBEEF"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 3735928559, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 0

def test_number_hex_lowercase() -> None:
    input_num_string = "0xdeadbeef"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 3735928559, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 0

def test_number_hex_underscore() -> None:
    input_num_string = "0xdead_beef"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 3735928559, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 0

def test_number_octal() -> None:
    input_num_string = "0o377"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 255, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 0

def test_number_binary() -> None:
    input_num_string = "0b10101010"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 170, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 0

def test_number_float() -> None:
    input_num_string = "3.1415"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 3.1415, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 0

def float_exponent() -> None:
    input_num_string = "5e+22"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 5e+22, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 0

def float_negative_exponent() -> None:
    input_num_string = "1e-2"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 1e-2, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 0

def float_positive_exponent() -> None:
    input_num_string = "1e+22"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 1e+2, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 0

def float_positive_capital_e() -> None:
    input_num_string = "1E+22"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 1e+2, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 0

def float_full_exponent() -> None:
    input_num_string = "6.626e-34"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 1e+2, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 0

def test_invalid_floats_predecimal() -> None:
    input_num_string = ".7"
    lexer = NumberLexer(input_num_string)
    with pytest.raises(ValueError):
        lexer.lex()

def test_invalid_floats_postdecimal() -> None:
    input_num_string = "7."
    lexer = NumberLexer(input_num_string)
    with pytest.raises(ValueError):
        lexer.lex()

def test_invalid_floats_exponent() -> None:
    input_num_string = "3.e+20"
    lexer = NumberLexer(input_num_string)
    with pytest.raises(ValueError):
        lexer.lex()

def test_float_underscore() -> None:
    input_num_string = "224_617.445_991_228"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 224617.445991228, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 0

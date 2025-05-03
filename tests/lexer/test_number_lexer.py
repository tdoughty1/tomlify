import pytest

from tomlify.lexer.number_lexer import NumberLexer
from tomlify.lexer.token import Token
from tomlify.lexer.token_type import TokenType

def test_number_int():
    input_num_string = "99"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 99.0, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 1

def test_number_int_zero():
    input_num_string = "0"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 0, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 1

def test_number_underscore():
    input_num_string = "1_000"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 1000, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 1

def test_number_multiple_underscore():
    input_num_string = "1_2_3_4_5"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 12345, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 1

def test_number_hex_uppercase():
    input_num_string = "0xDEADBEEF"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 3735928559, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 1

def test_number_hex_lowercase():
    input_num_string = "0xdeadbeef"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 3735928559, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 1

def test_number_hex_underscore():
    input_num_string = "0xdead_beef"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 3735928559, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 1

def test_number_octal():
    input_num_string = "0o377"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 255, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 1

def test_number_binary():
    input_num_string = "0b10101010"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 170, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 1

def test_number_float():
    input_num_string = "3.1415"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 3.1415, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 1

def float_exponent():
    input_num_string = "5e+22"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 5e+22, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 1

def float_negative_exponent():
    input_num_string = "1e-2"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 1e-2, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 1

def float_positive_exponent():
    input_num_string = "1e+22"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 1e+2, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 1

def float_positive_capital_e():
    input_num_string = "1E+22"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 1e+2, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 1

def float_full_exponent():
    input_num_string = "6.626e-34"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 1e+2, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 1

def test_invalid_floats_predecimal():
    input_num_string = ".7"
    lexer = NumberLexer(input_num_string)
    with pytest.raises(ValueError):
        lexer.lex()

def test_invalid_floats_postdecimal():
    input_num_string = "7."
    lexer = NumberLexer(input_num_string)
    with pytest.raises(ValueError):
        lexer.lex()

def test_invalid_floats_exponent():
    input_num_string = "3.e+20"
    lexer = NumberLexer(input_num_string)
    with pytest.raises(ValueError):
        lexer.lex()

def test_float_underscore():
    input_num_string = "224_617.445_991_228"
    lexer = NumberLexer(input_num_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.NUMBER, input_num_string, 224617.445991228, 1)]
    assert n_chars == len(input_num_string)
    assert n_lines == 1

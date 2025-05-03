from tomlify.lexer.identifier_lexer import IdentifierLexer
from tomlify.lexer.base_lexer import Token
from tomlify.lexer.base_lexer import TokenType

def test_identifier():
    input_string = "test"
    lexer = IdentifierLexer(input_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.IDENTIFIER, input_string, None, 1)]
    assert n_chars == len(input_string)
    assert n_lines == 1

def test_identifier_capital():
    input_string = "Test"
    lexer = IdentifierLexer(input_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.IDENTIFIER, input_string, None, 1)]
    assert n_chars == len(input_string)
    assert n_lines == 1

def test_identifier_number():
    input_string = "test1"
    lexer = IdentifierLexer(input_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.IDENTIFIER, input_string, None, 1)]
    assert n_chars == len(input_string)
    assert n_lines == 1

def test_identifier_underscore():
    input_string = "test_1"
    lexer = IdentifierLexer(input_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.IDENTIFIER, input_string, None, 1)]
    assert n_chars == len(input_string)
    assert n_lines == 1

def test_identifier_hyphen():
    input_string = "test-1"
    lexer = IdentifierLexer(input_string)
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.IDENTIFIER, input_string, None, 1)]
    assert n_chars == len(input_string)
    assert n_lines == 1

def test_identifier_ended_period():
    input_string = "test"
    lexer = IdentifierLexer(input_string+".test2")
    n_chars, n_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.IDENTIFIER, input_string, None, 1)]
    assert n_chars == len(input_string)
    assert n_lines == 1

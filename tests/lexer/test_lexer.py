# ruff: noqa: S101

from tests.helpers import (
    COMMENT_TOKEN,
    DOT_TOKEN,
    EOF_TOKEN,
    EQUAL_TOKEN,
    IDENTIFIER_TOKEN,
    NEWLINE_TOKEN,
    STRING_TOKEN,
)
from tomlify.lexer.lexer import Lexer


def test_scan_comment() -> None:
    input_string = "# This is a comment\n"
    lexer = Lexer(input_string)
    lexer.lex()
    actual_output = lexer.get_tokens()
    expected_output = [
        COMMENT_TOKEN("# This is a comment", " This is a comment", 1),
        NEWLINE_TOKEN(1),
        EOF_TOKEN(2),
    ]
    assert actual_output == expected_output

def test_scan_key_value() -> None:
    input_string = 'key = "value"\n'
    lexer = Lexer(input_string)
    lexer.lex()
    actual_output = lexer.get_tokens()
    expected_output = [
        IDENTIFIER_TOKEN("key", 1),
        EQUAL_TOKEN(1),
        STRING_TOKEN('"value"', "value", 1),
        NEWLINE_TOKEN(1),
        EOF_TOKEN(2),
    ]
    assert actual_output == expected_output


def test_basic_key() -> None:
    input_string = "key"
    lexer = Lexer(input_string)
    lexer.lex()
    actual_output = lexer.get_tokens()
    expected_output = [
        IDENTIFIER_TOKEN("key", 1),
        EOF_TOKEN(1),
    ]
    assert actual_output == expected_output

def test_basic_key_underscore() -> None:
    input_string = "key_underscore"
    lexer = Lexer(input_string)
    lexer.lex()
    actual_output = lexer.get_tokens()
    expected_output = [
        IDENTIFIER_TOKEN("key_underscore", 1),
        EOF_TOKEN(1),
    ]
    assert actual_output == expected_output

def test_basic_key_hyphen() -> None:
    input_string = "key-underscore"
    lexer = Lexer(input_string)
    lexer.lex()
    actual_output = lexer.get_tokens()
    expected_output = [
        IDENTIFIER_TOKEN("key-underscore", 1),
        EOF_TOKEN(1),
    ]
    assert actual_output == expected_output

def test_dotted_key() -> None:
    input_string = "key.value"
    lexer = Lexer(input_string)
    lexer.lex()
    actual_output = lexer.get_tokens()
    expected_output = [
        IDENTIFIER_TOKEN("key", 1),
        DOT_TOKEN(1),
        IDENTIFIER_TOKEN("value", 1),
        EOF_TOKEN(1),
    ]
    assert actual_output == expected_output

def test_dotted_quoted_key() -> None:
    input_string = 'site."google.com"'
    lexer = Lexer(input_string)
    lexer.lex()
    actual_output = lexer.get_tokens()
    expected_output = [
        IDENTIFIER_TOKEN("site", 1),
        DOT_TOKEN(1),
        STRING_TOKEN('"google.com"', "google.com", 1),
        EOF_TOKEN(1),
    ]
    assert actual_output == expected_output

def test_dotted_spaced_key() -> None:
    input_string = "fruit . flavor"
    lexer = Lexer(input_string)
    lexer.lex()
    actual_output = lexer.get_tokens()
    expected_output = [
        IDENTIFIER_TOKEN("fruit", 1),
        DOT_TOKEN(1),
        IDENTIFIER_TOKEN("flavor", 1),
        EOF_TOKEN(1),
    ]
    assert actual_output == expected_output

def test_basic_string() -> None:
    input_string = '"This is a string"\n'
    lexer = Lexer(input_string)
    lexer.lex()
    actual_output = lexer.get_tokens()
    expected_output = [
        STRING_TOKEN('"This is a string"', "This is a string", 1),
        NEWLINE_TOKEN(1),
        EOF_TOKEN(2),
    ]
    assert actual_output == expected_output

def test_basic_string_with_comment() -> None:
    input_string = '"This is a string # This is a comment"\n'
    lexer = Lexer(input_string)
    lexer.lex()
    actual_output = lexer.get_tokens()
    expected_output = [
        STRING_TOKEN(input_string.strip(), input_string.strip()[1:-1], 1),
        NEWLINE_TOKEN(1),
        EOF_TOKEN(2),
    ]
    assert actual_output == expected_output

def test_basic_string_dots() -> None:
    input_string = '"This is a string."'
    lexer = Lexer(input_string)
    lexer.lex()
    actual_output = lexer.get_tokens()
    expected_output = [
        STRING_TOKEN('"This is a string."', "This is a string.", 1),
        EOF_TOKEN(1),
    ]
    assert actual_output == expected_output

def test_basic_string_unicode() -> None:
    input_string = '"ʎǝʞ"'
    lexer = Lexer(input_string)
    lexer.lex()
    actual_output = lexer.get_tokens()
    expected_output = [
        STRING_TOKEN('"ʎǝʞ"', "ʎǝʞ", 1),
        EOF_TOKEN(1),
    ]
    assert actual_output == expected_output

def test_basic_string_apostrophe() -> None:
    input_string = "'This is a string.'"
    lexer = Lexer(input_string)
    lexer.lex()
    actual_output = lexer.get_tokens()
    expected_output = [
        STRING_TOKEN("'This is a string.'", "This is a string.", 1),
        EOF_TOKEN(1),
    ]
    assert actual_output == expected_output

def test_basic_string_multiline() -> None:
    input_string = r'"This is a string.\n Split over lines."'
    lexer = Lexer(input_string)
    lexer.lex()
    actual_output = lexer.get_tokens()
    expected_output = [
        STRING_TOKEN(input_string, input_string[1:-1], 1),
        EOF_TOKEN(1),
    ]
    assert actual_output == expected_output


def test_basic_string_containing_string() -> None:
    input_string = r'''"I'm a string. \"You can quote me\"."'''
    lexer = Lexer(input_string)
    lexer.lex()
    actual_output = lexer.get_tokens()
    expected_output = [
        STRING_TOKEN(input_string, input_string[1:-1], 1),
        EOF_TOKEN(1),
    ]
    assert actual_output == expected_output


def test_multiline_basic_string() -> None:
    input_string = '''"""This is a string.
    Split over lines."""'''
    lexer = Lexer(input_string)
    lexer.lex()
    actual_output = lexer.get_tokens()
    expected_output = [
        STRING_TOKEN(input_string, input_string[3:-3], 1),
        EOF_TOKEN(2),
    ]
    assert actual_output == expected_output

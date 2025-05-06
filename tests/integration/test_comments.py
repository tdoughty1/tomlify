# ruff: noqa: E501,S101,S603

from pathlib import Path
from subprocess import PIPE, Popen

RUNNER_FILE = "src/tomlify/lexer/lex_runner.py"
RESOURCE_PATH = "tests/resources"

def test_comments_toml() -> None:

    expected_tokens = [
    "Token(type_=<TokenType.COMMENT: 'COMMENT'>, lexeme='# This is a full-line comment', literal=' This is a full-line comment', line=1)",
    "Token(type_=<TokenType.NEWLINE: 'NEWLINE'>, lexeme='\\n', literal=None, line=1)",
    "Token(type_=<TokenType.IDENTIFIER: 'IDENTIFIER'>, lexeme='key', literal=None, line=2)",
    "Token(type_=<TokenType.EQUAL: 'EQUAL'>, lexeme='=', literal=None, line=2)",
    """Token(type_=<TokenType.STRING: 'STRING'>, lexeme='"value"', literal='value', line=2)""",
    "Token(type_=<TokenType.COMMENT: 'COMMENT'>, lexeme='# This is a comment at the end of a line', literal=' This is a comment at the end of a line', line=2)",
    "Token(type_=<TokenType.NEWLINE: 'NEWLINE'>, lexeme='\\n', literal=None, line=2)",
    "Token(type_=<TokenType.IDENTIFIER: 'IDENTIFIER'>, lexeme='another', literal=None, line=3)",
    "Token(type_=<TokenType.EQUAL: 'EQUAL'>, lexeme='=', literal=None, line=3)",
    """Token(type_=<TokenType.STRING: 'STRING'>, lexeme='"# This is not a comment"', literal='# This is not a comment', line=3)""",
    "Token(type_=<TokenType.NEWLINE: 'NEWLINE'>, lexeme='\\n', literal=None, line=3)",
    "Token(type_=<TokenType.EOF: 'EOF'>, lexeme='', literal=None, line=4)",
    ]

    test_file = Path(RESOURCE_PATH) / "comments" / "comments.toml"
    command = ["uv", "run", RUNNER_FILE, str(test_file)]
    process = Popen(command, stdout=PIPE, stderr=PIPE, text=True)
    out, err = process.communicate()

    actual_tokens = out.splitlines()

    assert process.returncode == 0
    assert err == ""
    assert actual_tokens == expected_tokens

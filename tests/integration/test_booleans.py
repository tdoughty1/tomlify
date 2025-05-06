# ruff: noqa: E501,S101,S603

from pathlib import Path
from subprocess import PIPE, Popen

RUNNER_FILE = "src/tomlify/lexer/lex_runner.py"
RESOURCE_PATH = "tests/resources"

def test_booleans_toml() -> None:

    expected_tokens = [
        "Token(type_=<TokenType.IDENTIFIER: 'IDENTIFIER'>, lexeme='bool1', literal=None, line=1)",
        "Token(type_=<TokenType.EQUAL: 'EQUAL'>, lexeme='=', literal=None, line=1)",
        "Token(type_=<TokenType.BOOLEAN: 'BOOLEAN'>, lexeme='true', literal=True, line=1)",
        "Token(type_=<TokenType.NEWLINE: 'NEWLINE'>, lexeme='\\n', literal=None, line=1)",
        "Token(type_=<TokenType.IDENTIFIER: 'IDENTIFIER'>, lexeme='bool2', literal=None, line=2)",
        "Token(type_=<TokenType.EQUAL: 'EQUAL'>, lexeme='=', literal=None, line=2)",
        "Token(type_=<TokenType.BOOLEAN: 'BOOLEAN'>, lexeme='false', literal=False, line=2)",
        "Token(type_=<TokenType.NEWLINE: 'NEWLINE'>, lexeme='\\n', literal=None, line=2)",
        "Token(type_=<TokenType.EOF: 'EOF'>, lexeme='', literal=None, line=3)",
    ]

    test_file = Path(RESOURCE_PATH) / "booleans" / "booleans.toml"
    command = ["uv", "run", RUNNER_FILE, str(test_file)]
    process = Popen(command, stdout=PIPE, stderr=PIPE, text=True)
    out, err = process.communicate()

    actual_tokens = out.splitlines()

    assert process.returncode == 0
    assert err == ""
    assert actual_tokens == expected_tokens


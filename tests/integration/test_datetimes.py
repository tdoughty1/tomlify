# ruff: noqa: E501,S101,S603

from pathlib import Path
from subprocess import PIPE, Popen

RUNNER_FILE = "src/tomlify/lexer/lex_runner.py"
RESOURCE_PATH = "tests/resources"

def test_dates_toml() -> None:

    expected_tokens = [
        "Token(type_=<TokenType.IDENTIFIER: 'IDENTIFIER'>, lexeme='ld1', literal=None, line=1)",
        "Token(type_=<TokenType.EQUAL: 'EQUAL'>, lexeme='=', literal=None, line=1)",
        "Token(type_=<TokenType.DATE: 'DATE'>, lexeme='1979-05-27', literal=datetime.date(1979, 5, 27), line=1)",
        "Token(type_=<TokenType.NEWLINE: 'NEWLINE'>, lexeme='\\n', literal=None, line=1)",
        "Token(type_=<TokenType.EOF: 'EOF'>, lexeme='', literal=None, line=2)",
    ]

    test_file = Path(RESOURCE_PATH) / "datetimes" / "dates.toml"
    command = ["uv", "run", RUNNER_FILE, str(test_file)]
    process = Popen(command, stdout=PIPE, stderr=PIPE, text=True)
    out, err = process.communicate()

    actual_tokens = out.splitlines()

    assert process.returncode == 0
    assert err == ""
    assert actual_tokens == expected_tokens

def test_local_datetimes_toml() -> None:

    expected_tokens = [
        "Token(type_=<TokenType.IDENTIFIER: 'IDENTIFIER'>, lexeme='ldt1', literal=None, line=1)",
        "Token(type_=<TokenType.EQUAL: 'EQUAL'>, lexeme='=', literal=None, line=1)",
        "Token(type_=<TokenType.DATE: 'DATE'>, lexeme='1979-05-27T07:32:00', literal=datetime.datetime(1979, 5, 27, 7, 32), line=1)",
        "Token(type_=<TokenType.NEWLINE: 'NEWLINE'>, lexeme='\\n', literal=None, line=1)",
        "Token(type_=<TokenType.IDENTIFIER: 'IDENTIFIER'>, lexeme='ldt2', literal=None, line=2)",
        "Token(type_=<TokenType.EQUAL: 'EQUAL'>, lexeme='=', literal=None, line=2)",
        "Token(type_=<TokenType.DATE: 'DATE'>, lexeme='1979-05-27T00:32:00.999999', literal=datetime.datetime(1979, 5, 27, 0, 32, 0, 999999), line=2)",
        "Token(type_=<TokenType.NEWLINE: 'NEWLINE'>, lexeme='\\n', literal=None, line=2)",
        "Token(type_=<TokenType.EOF: 'EOF'>, lexeme='', literal=None, line=3)",
    ]

    test_file = Path(RESOURCE_PATH) / "datetimes" / "local_datetimes.toml"
    command = ["uv", "run", RUNNER_FILE, str(test_file)]
    process = Popen(command, stdout=PIPE, stderr=PIPE, text=True)
    out, err = process.communicate()

    actual_tokens = out.splitlines()

    assert process.returncode == 0
    assert err == ""
    assert actual_tokens == expected_tokens

def test_offset_datetimes_toml() -> None:

    expected_tokens = [
        "Token(type_=<TokenType.IDENTIFIER: 'IDENTIFIER'>, lexeme='odt1', literal=None, line=1)",
        "Token(type_=<TokenType.EQUAL: 'EQUAL'>, lexeme='=', literal=None, line=1)",
        "Token(type_=<TokenType.DATE: 'DATE'>, lexeme='1979-05-27T07:32:00Z', literal=datetime.datetime(1979, 5, 27, 7, 32, tzinfo=datetime.timezone.utc), line=1)",
        "Token(type_=<TokenType.NEWLINE: 'NEWLINE'>, lexeme='\\n', literal=None, line=1)",
        "Token(type_=<TokenType.IDENTIFIER: 'IDENTIFIER'>, lexeme='odt2', literal=None, line=2)",
        "Token(type_=<TokenType.EQUAL: 'EQUAL'>, lexeme='=', literal=None, line=2)",
        "Token(type_=<TokenType.DATE: 'DATE'>, lexeme='1979-05-27T00:32:00-07:00', literal=datetime.datetime(1979, 5, 27, 0, 32, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200))), line=2)",
        "Token(type_=<TokenType.NEWLINE: 'NEWLINE'>, lexeme='\\n', literal=None, line=2)",
        "Token(type_=<TokenType.IDENTIFIER: 'IDENTIFIER'>, lexeme='odt3', literal=None, line=3)",
        "Token(type_=<TokenType.EQUAL: 'EQUAL'>, lexeme='=', literal=None, line=3)",
        "Token(type_=<TokenType.DATE: 'DATE'>, lexeme='1979-05-27T00:32:00.999999-07:00', literal=datetime.datetime(1979, 5, 27, 0, 32, 0, 999999, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200))), line=3)",
        "Token(type_=<TokenType.NEWLINE: 'NEWLINE'>, lexeme='\\n', literal=None, line=3)",
        "Token(type_=<TokenType.NEWLINE: 'NEWLINE'>, lexeme='\\n', literal=None, line=4)",
        "Token(type_=<TokenType.IDENTIFIER: 'IDENTIFIER'>, lexeme='odt4', literal=None, line=5)",
        "Token(type_=<TokenType.EQUAL: 'EQUAL'>, lexeme='=', literal=None, line=5)",
        "Token(type_=<TokenType.DATE: 'DATE'>, lexeme='1979-05-27 07:32:00Z', literal=datetime.datetime(1979, 5, 27, 7, 32, tzinfo=datetime.timezone.utc), line=5)",
        "Token(type_=<TokenType.NEWLINE: 'NEWLINE'>, lexeme='\\n', literal=None, line=5)",
        "Token(type_=<TokenType.EOF: 'EOF'>, lexeme='', literal=None, line=6)",
    ]

    test_file = Path(RESOURCE_PATH) / "datetimes" / "offset_datetimes.toml"
    command = ["uv", "run", RUNNER_FILE, str(test_file)]
    process = Popen(command, stdout=PIPE, stderr=PIPE, text=True)
    out, err = process.communicate()

    actual_tokens = out.splitlines()

    assert process.returncode == 0
    assert err == ""
    assert actual_tokens == expected_tokens

def test_times_toml() -> None:

    expected_tokens = [
        "Token(type_=<TokenType.IDENTIFIER: 'IDENTIFIER'>, lexeme='lt1', literal=None, line=1)",
        "Token(type_=<TokenType.EQUAL: 'EQUAL'>, lexeme='=', literal=None, line=1)",
        "Token(type_=<TokenType.DATE: 'DATE'>, lexeme='07:32:00', literal=datetime.time(7, 32), line=1)",
        "Token(type_=<TokenType.NEWLINE: 'NEWLINE'>, lexeme='\\n', literal=None, line=1)",
        "Token(type_=<TokenType.IDENTIFIER: 'IDENTIFIER'>, lexeme='lt2', literal=None, line=2)",
        "Token(type_=<TokenType.EQUAL: 'EQUAL'>, lexeme='=', literal=None, line=2)",
        "Token(type_=<TokenType.DATE: 'DATE'>, lexeme='00:32:00.999999', literal=datetime.time(0, 32, 0, 999999), line=2)",
        "Token(type_=<TokenType.NEWLINE: 'NEWLINE'>, lexeme='\\n', literal=None, line=2)",
        "Token(type_=<TokenType.EOF: 'EOF'>, lexeme='', literal=None, line=3)",
    ]

    test_file = Path(RESOURCE_PATH) / "datetimes" / "times.toml"
    command = ["uv", "run", RUNNER_FILE, str(test_file)]
    process = Popen(command, stdout=PIPE, stderr=PIPE, text=True)
    out, err = process.communicate()

    actual_tokens = out.splitlines()

    assert process.returncode == 0
    assert err == ""
    assert actual_tokens == expected_tokens

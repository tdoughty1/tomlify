from pathlib import Path

from tests.integration.runner import RESOURCE_PATH, run_test

SCRIPT_PATH = Path("src/tomlify/parser/parse_runner.py")

def test_parse_basic_strings_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "strings" / "basic_strings.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_literal_strings_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "strings" / "literal_strings.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_multiline_literal_strings_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "strings" / "multiline_literal_strings.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_multiline_strings_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "strings" / "multiline_strings.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

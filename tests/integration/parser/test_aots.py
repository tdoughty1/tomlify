from pathlib import Path

from tests.integration.runner import RESOURCE_PATH, run_test

SCRIPT_PATH = Path("src/tomlify/parser/parse_runner.py")

def test_parse_aots_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "aots" / "aots.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_aots_2_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "aots" / "aots_2.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_inline_aots_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "aots" / "inline_aots.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_invalid_aots_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "aots" / "invalid_aots.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

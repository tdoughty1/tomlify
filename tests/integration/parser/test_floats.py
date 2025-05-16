from pathlib import Path

from tests.integration.runner import RESOURCE_PATH, run_test

SCRIPT_PATH = Path("src/tomlify/parser/parse_runner.py")

def test_parse_floats_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "floats" / "floats.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_invalid_floats_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "floats" / "invalid_floats.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_special_floats_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "floats" / "special_floats.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_underscore_floats_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "floats" / "underscore_floats.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

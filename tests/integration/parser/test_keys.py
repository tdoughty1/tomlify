from pathlib import Path

from tests.integration.runner import RESOURCE_PATH, run_test

SCRIPT_PATH = Path("src/tomlify/parser/parse_runner.py")

def test_parse_bare_keys_toml() -> None:
    
    expected_exprs = [
        'KeyValue(key = "value")',
        'KeyValue(bare_key = "value")',
        'KeyValue(bare-key = "value")',
        'KeyValue(1234 = "value")',
    ]

    test_path = Path(RESOURCE_PATH) / "keys" / "bare_keys.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_dotted_keys_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "keys" / "dotted_keys.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_dotted_keys_2_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "keys" / "dotted_keys_2.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_dotted_keys_3_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "keys" / "dotted_keys_3.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_duplicate_keys_toml() -> None:
    
    expected_exprs = [
        'KeyValue(name = Tom)',
        'KeyValue(name = Pradyun)',
    ]

    test_path = Path(RESOURCE_PATH) / "keys" / "duplicate_keys.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_numeric_keys_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "keys" / "numeric_keys.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_order_keys_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "keys" / "order_keys.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_quoted_keys_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "keys" / "quoted_keys.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

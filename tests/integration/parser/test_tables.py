from pathlib import Path

from tests.integration.runner import RESOURCE_PATH, run_test

SCRIPT_PATH = Path("src/tomlify/parser/parse_runner.py")

def test_parse_dotted_tables_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "tables" / "dotted_tables.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_inline_tables_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "tables" / "inline_tables.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_invalid_inline_tables_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "tables" / "invalid_inline_tables.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_invalid_tables_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "tables" / "invalid_tables.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_levelled_tables_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "tables" / "levelled_tables.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_named_tables_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "tables" / "named_tables.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_ordered_tables_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "tables" / "ordered_tables.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_tables_toml() -> None:
    
    expected_exprs = [
        'KeyValue(bool1 = True)',
        'KeyValue(bool2 = False)',
    ]

    test_path = Path(RESOURCE_PATH) / "tables" / "tables.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_top_tables_toml() -> None:
    
    expected_exprs = [
        'KeyValue(name = Fido)',
        'KeyValue(breed = pug)',

    ]

    test_path = Path(RESOURCE_PATH) / "tables" / "top_tables.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

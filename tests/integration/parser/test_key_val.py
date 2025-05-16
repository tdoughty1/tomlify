from pathlib import Path

from tests.integration.runner import RESOURCE_PATH, run_test

SCRIPT_PATH = Path("src/tomlify/parser/parse_runner.py")

def test_parse_key_val_toml() -> None:
    
    expected_exprs = [
        'KeyValue(key = value)'
    ]

    test_path = Path(RESOURCE_PATH) / "key_value.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

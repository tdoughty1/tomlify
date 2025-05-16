from pathlib import Path

from tests.integration.runner import RESOURCE_PATH, run_test

SCRIPT_PATH = Path("src/tomlify/parser/parse_runner.py")

def test_parse_dates_toml() -> None:
    
    expected_exprs = [
        'KeyValue(ld1 = 1979-05-27)',
    ]

    test_path = Path(RESOURCE_PATH) / "datetimes" / "dates.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_local_datetimes_toml() -> None:
    
    expected_exprs = [
        'KeyValue(ld1 = 1979-05-27)',
    ]

    test_path = Path(RESOURCE_PATH) / "datetimes" / "local_datetimes.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_offset_datetimes_toml() -> None:
    
    expected_exprs = [
        'KeyValue(ld1 = 1979-05-27)',
    ]

    test_path = Path(RESOURCE_PATH) / "datetimes" / "offset_datetimes.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

def test_parse_times_toml() -> None:
    
    expected_exprs = [
        'KeyValue(ld1 = 1979-05-27)',
    ]

    test_path = Path(RESOURCE_PATH) / "datetimes" / "times.toml"
    out, err, return_code = run_test(SCRIPT_PATH, test_path)

    actual_tokens = out.splitlines()

    assert return_code == 0
    assert err == ""
    assert actual_tokens == expected_exprs

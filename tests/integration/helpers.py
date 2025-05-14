# ruff: noqa: S603

from pathlib import Path
from subprocess import PIPE, Popen

RESOURCE_PATH = "tests/resources"
RUNNER_FILE = "src/tomlify/lexer/lex_runner.py"

def run_test(test_file: Path) -> tuple[str, str, int]:
    command = ["uv", "run", RUNNER_FILE, "--lex", str(test_file)]
    process = Popen(command, stdout=PIPE, stderr=PIPE, text=True)
    out, err = process.communicate()
    code = process.returncode
    return (out, err, code)

#ruff: noqa: FBT001, FBT003
from pathlib import Path

import typer

from tomlify.lexer.lexer import Lexer
from tomlify.parser.parser import Parser


def run(source: str) -> None:
    lexer = Lexer(source)
    lexer.lex()
    tokens = lexer.get_tokens()
    parser = Parser(tokens)
    expressions = parser.parse()
    for expression in expressions:
        typer.echo(expression)

def run_file(path: Path) -> None:
    with Path.open(path) as f:
        run(f.read())

def main(path: str) -> None:
    run_file(Path(path))

if __name__ == "__main__":
    typer.run(main)

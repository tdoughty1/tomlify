from pathlib import Path

import typer

from tomlify.lexer.lexer import Lexer
from tomlify.parser.parser import Parser


def run(source: str, lex_only: bool) -> None:
    lexer = Lexer(source)
    lexer.lex()
    tokens = lexer.get_tokens()
    if lex_only:
        for token in tokens:
            print(f"{token}")
    if not lex_only:
        parser = Parser(tokens)
        expressions = parser.parse()
        for expression in expressions:
            typer.echo(expression)

def run_file(path: Path, lex_only: bool) -> None:
    with Path.open(path) as f:
        run(f.read(), lex_only)

lex_option = typer.Option(False, "--lex", help="Only Run Lexer on input file")

def main(path: str, lex_only: bool = lex_option) -> None:
    run_file(Path(path), lex_only)


#if __name__ == "__main__":

    #EXPECTED_ARGS = 2
    #if len(sys.argv) != EXPECTED_ARGS:
    #    print("Usage: python3 -m tomlify.lexer.lex_runner <filename>") # noqa: T201
    #    sys.exit(1)

    #typer.run(main())

# TODO: Move to typer command line functionality
# TODO: Allow command line argument to just run lexer


if __name__ == "__main__":
    typer.run(main)

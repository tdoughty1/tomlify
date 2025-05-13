import sys
from pathlib import Path

from tomlify.lexer.lexer import Lexer
from tomlify.parser.parser import Parser


def run(source: str) -> None:
    lexer = Lexer(source)
    lexer.lex()
    tokens = lexer.get_tokens()
    for token in tokens:
        print(f"{token}")
    #parser = Parser(tokens)
    #expressions = parser.parse()
    #for expression in expressions:
        #print(expression) # noqa: T201

def run_file(path: Path) -> None:
    with Path.open(path) as f:
        run(f.read())

def main(path: Path) -> None:
    run_file(path)

if __name__ == "__main__":

    EXPECTED_ARGS = 2

    if len(sys.argv) != EXPECTED_ARGS:
        print("Usage: python3 -m tomlify.lexer.lex_runner <filename>") # noqa: T201
        sys.exit(1)

    main(Path(sys.argv[1]))

# TODO: Move to typer command line functionality
# TODO: Allow command line argument to just run lexer

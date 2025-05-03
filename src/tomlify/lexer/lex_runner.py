import sys

from tomlify.lexer.lexer import Lexer


def run(source: str) -> None:
    lexer = Lexer(source)
    lexer.lexTokens()
    with open("tokens.txt", "w") as f:
        for token in lexer._tokens:
            f.write(f"{token}\n")

def runFile(path: str) -> None:
    with open(path, 'r') as f:
        run(f.read())

def main(path: str) -> None:
    runFile(path)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 -m tomlify.lexer.lex_runner <filename>")
        sys.exit(1)
    
    main(sys.argv[1])

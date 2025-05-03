import sys

from tomlify.lexer.scanner import Scanner



def run(source):
    scanner = Scanner(source)
    scanner.scanTokens()
    with open("tokens.txt", "w") as f:
        for token in scanner.tokens:
            f.write(f"{token}\n")
    return


def runFile(path):
    with open(path, 'r') as f:
        run(f.read())

def main(path):
    runFile(path)

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python3 -m tomlify.lexer.lex_runner <filename>")
        sys.exit(1)
    
    main(sys.argv[1])

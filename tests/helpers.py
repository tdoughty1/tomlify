from tomlify.lexer.token import Token 
from tomlify.lexer.token_type import TokenType

def EQUAL_TOKEN(line):
    return Token(TokenType.EQUAL, '=', None, line)

def NEWLINE_TOKEN(line): 
    return Token(TokenType.NEWLINE, '\n', None, line)
 
def EOF_TOKEN(line):
    return Token(TokenType.EOF, '', None, line)

def STRING_TOKEN(value, literal, line):
    return Token(TokenType.STRING, value, literal, line)

def IDENTIFIER_TOKEN(value, line):
    return Token(TokenType.IDENTIFIER, value, None, line)

def COMMENT_TOKEN(value, literal, line):
    return Token(TokenType.COMMENT, value, literal, line)

def DOT_TOKEN(line):
    return Token(TokenType.DOT, '.', None, line)
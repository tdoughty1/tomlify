from enum import Enum

class TokenType(Enum):
  
    #Single-character tokens.
    LEFT_PAREN = "LEFT_PAREN"
    RIGHT_PAREN = "RIGHT_PAREN"
    LEFT_BRACE = "LEFT_BRACE"
    RIGHT_BRACE = "RIGHT_BRACE"
    LEFT_BRACKET = "LEFT_BRACKET"
    RIGHT_BRACKET = "RIGHT_BRACKET"
    COMMA = "COMMA"
    DOT = "DOT"
    MINUS = "MINUS"
    PLUS = "PLUS"
    SLASH = "SLASH"
    EQUAL = "EQUAL"
    COLON = "COLON"

    # Literals.
    IDENTIFIER = "IDENTIFIER"
    STRING = "STRING"
    NUMBER = "NUMBER"
    COMMENT = "COMMENT"

    # Control Characters
    NEWLINE = "NEWLINE"

    # Terminal Character
    EOF = "EOF"

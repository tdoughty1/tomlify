from tomlify.lexer.comment_lexer import CommentLexer
from tomlify.lexer.token import Token
from tomlify.lexer.token_type import TokenType

def test_lex_comment() -> None:
    input_comment = "# This is a comment"
    lexer = CommentLexer(input_comment)
    num_chars, num_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.COMMENT, input_comment, input_comment[1:], 1)]
    assert num_chars == len(input_comment)
    assert num_lines == 0
                        
def test_lex_comment_with_escaped_newline() -> None:
    input_comment = "# This is another comment"
    lexer = CommentLexer(f"{input_comment}\nNon-Comment Line")
    num_chars, num_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.COMMENT, input_comment, input_comment[1:], 1)]
    assert num_chars == 25
    assert num_lines == 0

def test_lex_comment_with_actual_newline() -> None:
    input_comment = "# This is a third comment"
    lexer = CommentLexer(
        f"""{input_comment}
        Non-Comment Line"""
    )
    num_chars, num_lines = lexer.lex()
    assert lexer._tokens == [Token(TokenType.COMMENT, input_comment, input_comment[1:], 1)]
    assert num_chars == 25
    assert num_lines == 0

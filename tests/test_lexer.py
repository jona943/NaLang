# tests/test_lexer.py

import unittest
from src.interpreter import Lexer, TokenType

class TestLexer(unittest.TestCase):
    def test_keywords(self):
        source_code = "if else while for return"
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        expected_tokens = [
            (TokenType.KEYWORD, "if"),
            (TokenType.KEYWORD, "else"),
            (TokenType.KEYWORD, "while"),
            (TokenType.KEYWORD, "for"),
            (TokenType.KEYWORD, "return"),
            (TokenType.EOF, "")
        ]
        self.assertTokens(tokens, expected_tokens)

    def test_identifiers(self):
        source_code = "variable_name anotherVariable _privateVar"
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        expected_tokens = [
            (TokenType.IDENTIFIER, "variable_name"),
            (TokenType.IDENTIFIER, "anotherVariable"),
            (TokenType.IDENTIFIER, "_privateVar"),
            (TokenType.EOF, "")
        ]
        self.assertTokens(tokens, expected_tokens)

    def test_numbers(self):
        source_code = "123 456.789"
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        expected_tokens = [
            (TokenType.NUMBER, "123"),
            (TokenType.NUMBER, "456.789"),
            (TokenType.EOF, "")
        ]
        self.assertTokens(tokens, expected_tokens)

    def test_strings(self):
        source_code = '"hello" "world"'
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        expected_tokens = [
            (TokenType.STRING, '"hello"'),
            (TokenType.STRING, '"world"'),
            (TokenType.EOF, "")
        ]
        self.assertTokens(tokens, expected_tokens)

    def test_operators(self):
        source_code = "+ - * / ="
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        expected_tokens = [
            (TokenType.OPERATOR, "+"),
            (TokenType.OPERATOR, "-"),
            (TokenType.OPERATOR, "*"),
            (TokenType.OPERATOR, "/"),
            (TokenType.OPERATOR, "="),
            (TokenType.EOF, "")
        ]
        self.assertTokens(tokens, expected_tokens)

    def test_delimiters(self):
        source_code = "( ) { } , ;"
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        expected_tokens = [
            (TokenType.DELIMITER, "("),
            (TokenType.DELIMITER, ")"),
            (TokenType.DELIMITER, "{"),
            (TokenType.DELIMITER, "}"),
            (TokenType.DELIMITER, ","),
            (TokenType.DELIMITER, ";"),
            (TokenType.EOF, "")
        ]
        self.assertTokens(tokens, expected_tokens)

    def assertTokens(self, tokens, expected_tokens):
        self.assertEqual(len(tokens), len(expected_tokens))
        for token, expected in zip(tokens, expected_tokens):
            self.assertEqual((token.type, token.value), expected)

if __name__ == "__main__":
    unittest.main()

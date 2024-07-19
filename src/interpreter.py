# src/interpreter.py

import re
from enum import Enum, auto

class TokenType(Enum):
    KEYWORD = auto()
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()
    OPERATOR = auto()
    DELIMITER = auto()
    WHITESPACE = auto()
    COMMENT = auto()
    EOF = auto()

class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type}, {self.value}, {self.line}, {self.column})"

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.current_position = 0
        self.current_line = 1
        self.current_column = 1

        self.token_patterns = [
            (TokenType.KEYWORD, r'\b(if|else|while|for|return)\b'),
            (TokenType.IDENTIFIER, r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
            (TokenType.NUMBER, r'\b\d+(\.\d+)?\b'),
            (TokenType.STRING, r'"([^"\\]|\\.)*"'),
            (TokenType.OPERATOR, r'[+\-*/=<>!]+'),
            (TokenType.DELIMITER, r'[(),;{}]'),
            (TokenType.WHITESPACE, r'\s+'),
            (TokenType.COMMENT, r'//.*|/\*[\s\S]*?\*/'),
        ]

    def next_token(self):
        if self.current_position >= len(self.source_code):
            return Token(TokenType.EOF, '', self.current_line, self.current_column)

        for token_type, pattern in self.token_patterns:
            regex = re.compile(pattern)
            match = regex.match(self.source_code, self.current_position)
            if match:
                value = match.group(0)
                token = Token(token_type, value, self.current_line, self.current_column)
                self.current_position += len(value)
                self.update_position(value)
                if token_type != TokenType.WHITESPACE and token_type != TokenType.COMMENT:
                    return token

        # If no pattern matches, raise an error
        raise SyntaxError(f"Unexpected character at line {self.current_line} column {self.current_column}")

    def update_position(self, value):
        lines = value.split('\n')
        if len(lines) > 1:
            self.current_line += len(lines) - 1
            self.current_column = len(lines[-1]) + 1
        else:
            self.current_column += len(value)

    def tokenize(self):
        tokens = []
        while True:
            token = self.next_token()
            tokens.append(token)
            if token.type == TokenType.EOF:
                break
        return tokens

if __name__ == "__main__":
    source_code = """
    if (x < 10) {
        return x + 1;
    } else {
        return x - 1;
    }
    """
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    for token in tokens:
        print(token)

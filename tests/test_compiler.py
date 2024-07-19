# src/compiler.py

from interpreter import Lexer, TokenType

class ASTNode:
    pass

class BinOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class NumNode(ASTNode):
    def __init__(self, value):
        self.value = value

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.current_token = self.tokens[self.current_token_index]

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token_index += 1
            if self.current_token_index < len(self.tokens):
                self.current_token = self.tokens[self.current_token_index]
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token.type}")

    def factor(self):
        token = self.current_token
        if token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return NumNode(float(token.value))
        elif token.type == TokenType.IDENTIFIER:
            self.eat(TokenType.IDENTIFIER)
            return NumNode(token.value)
        else:
            raise SyntaxError(f"Unexpected token: {token.type}")

    def term(self):
        node = self.factor()
        while self.current_token.type in (TokenType.OPERATOR,) and self.current_token.value in ('*', '/'):
            token = self.current_token
            if token.value == '*':
                self.eat(TokenType.OPERATOR)
            elif token.value == '/':
                self.eat(TokenType.OPERATOR)
            node = BinOpNode(left=node, op=token.value, right=self.factor())
        return node

    def expr(self):
        node = self.term()
        while self.current_token.type in (TokenType.OPERATOR,) and self.current_token.value in ('+', '-'):
            token = self.current_token
            if token.value == '+':
                self.eat(TokenType.OPERATOR)
            elif token.value == '-':
                self.eat(TokenType.OPERATOR)
            node = BinOpNode(left=node, op=token.value, right=self.term())
        return node

    def parse(self):
        return self.expr()

class Interpreter:
    def visit(self, node):
        if isinstance(node, NumNode):
            return node.value
        elif isinstance(node, BinOpNode):
            if node.op == '+':
                return self.visit(node.left) + self.visit(node.right)
            elif node.op == '-':
                return self.visit(node.left) - self.visit(node.right)
            elif node.op == '*':
                return self.visit(node.left) * self.visit(node.right)
            elif node.op == '/':
                return self.visit(node.left) / self.visit(node.right)
        else:
            raise TypeError(f"Unknown AST node type: {type(node)}")

class Compiler:
    def __init__(self, source_code):
        self.source_code = source_code

    def compile(self):
        # Lexical analysis
        lexer = Lexer(self.source_code)
        tokens = lexer.tokenize()

        # Parsing
        parser = Parser(tokens)
        ast = parser.parse()

        # Evaluation
        interpreter = Interpreter()
        result = interpreter.visit(ast)
        
        return result

if __name__ == "__main__":
    source_code = """
    3 + 5 * (10 - 4);
    """
    compiler = Compiler(source_code)
    result = compiler.compile()
    print("Result:", result)

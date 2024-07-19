# tests/test_parser.py

import unittest
from src.compiler import Parser, Lexer, BinOpNode, NumNode, TokenType

class TestParser(unittest.TestCase):
    def parse(self, source_code):
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        return parser.parse()

    def test_single_number(self):
        source_code = "42"
        ast = self.parse(source_code)
        expected_ast = NumNode(42)
        self.assertEqual(ast.value, expected_ast.value)

    def test_simple_addition(self):
        source_code = "3 + 5"
        ast = self.parse(source_code)
        expected_ast = BinOpNode(left=NumNode(3), op='+', right=NumNode(5))
        self.assertBinOpNode(ast, expected_ast)

    def test_simple_subtraction(self):
        source_code = "10 - 4"
        ast = self.parse(source_code)
        expected_ast = BinOpNode(left=NumNode(10), op='-', right=NumNode(4))
        self.assertBinOpNode(ast, expected_ast)

    def test_simple_multiplication(self):
        source_code = "7 * 6"
        ast = self.parse(source_code)
        expected_ast = BinOpNode(left=NumNode(7), op='*', right=NumNode(6))
        self.assertBinOpNode(ast, expected_ast)

    def test_simple_division(self):
        source_code = "8 / 2"
        ast = self.parse(source_code)
        expected_ast = BinOpNode(left=NumNode(8), op='/', right=NumNode(2))
        self.assertBinOpNode(ast, expected_ast)

    def test_complex_expression(self):
        source_code = "3 + 5 * (10 - 4)"
        ast = self.parse(source_code)
        expected_ast = BinOpNode(
            left=NumNode(3),
            op='+',
            right=BinOpNode(
                left=NumNode(5),
                op='*',
                right=BinOpNode(left=NumNode(10), op='-', right=NumNode(4))
            )
        )
        self.assertBinOpNode(ast, expected_ast)

    def assertBinOpNode(self, actual, expected):
        self.assertIsInstance(actual, BinOpNode)
        self.assertEqual(actual.op, expected.op)
        self.assertEqual(actual.left.value, expected.left.value)
        self.assertEqual(actual.right.value, expected.right.value)

if __name__ == "__main__":
    unittest.main()

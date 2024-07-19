# tests/test_interpreter.py

import unittest
from src.compiler import Compiler

class TestInterpreter(unittest.TestCase):
    def evaluate(self, source_code):
        compiler = Compiler(source_code)
        return compiler.compile()

    def test_single_number(self):
        source_code = "42"
        result = self.evaluate(source_code)
        self.assertEqual(result, 42)

    def test_simple_addition(self):
        source_code = "3 + 5"
        result = self.evaluate(source_code)
        self.assertEqual(result, 8)

    def test_simple_subtraction(self):
        source_code = "10 - 4"
        result = self.evaluate(source_code)
        self.assertEqual(result, 6)

    def test_simple_multiplication(self):
        source_code = "7 * 6"
        result = self.evaluate(source_code)
        self.assertEqual(result, 42)

    def test_simple_division(self):
        source_code = "8 / 2"
        result = self.evaluate(source_code)
        self.assertEqual(result, 4)

    def test_complex_expression(self):
        source_code = "3 + 5 * (10 - 4)"
        result = self.evaluate(source_code)
        self.assertEqual(result, 33)

if __name__ == "__main__":
    unittest.main()

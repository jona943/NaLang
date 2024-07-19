# src/repl.py

from compiler import Compiler

class REPL:
    def __init__(self):
        self.compiler = Compiler("")

    def start(self):
        print("Welcome to the NaLang REPL!")
        print("Type 'exit' to quit.")
        while True:
            try:
                source_code = input("NaLang> ")
                if source_code.lower() in {"exit", "quit"}:
                    print("Goodbye!")
                    break
                self.compiler.source_code = source_code
                ast = self.compiler.compile()
                print("AST:", ast)
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    repl = REPL()
    repl.start()

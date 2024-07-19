# src/lexer.py

import re

# Definir los tipos de tokens
TOKEN_TYPES = [
    ("PALABRA_CLAVE", r'\b(si|sino|mientras|para|función|clase|retornar|imprimir|verdadero|falso)\b'),
    ("IDENTIFICADOR", r'\b[A-Za-z_][A-Za-z0-9_]*\b'),
    ("NUMERO", r'\b\d+(\.\d+)?\b'),
    ("CADENA", r'"[^"]*"'),
    ("OPERADOR", r'[+\-*/%]'),
    ("PARENTESIS_IZQUIERDO", r'\('),
    ("PARENTESIS_DERECHO", r'\)'),
    ("LLAVE_IZQUIERDA", r'\{'),
    ("LLAVE_DERECHA", r'\}'),
    ("IGUAL", r'='),
    ("PUNTO_Y_COMA", r';'),
    ("COMA", r','),
    ("ESPACIO", r'\s+'),
    ("DESCONOCIDO", r'.'),
]

class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
    
    def __repr__(self):
        return f"Token({self.tipo}, {self.valor})"

class Lexer:
    def __init__(self, codigo):
        self.codigo = codigo
        self.posicion = 0
        self.tokens = []
    
    def analizar(self):
        while self.posicion < len(self.codigo):
            token = self.obtener_siguiente_token()
            if token:
                self.tokens.append(token)
        return self.tokens
    
    def obtener_siguiente_token(self):
        if self.posicion >= len(self.codigo):
            return None
        
        for token_type, pattern in TOKEN_TYPES:
            regex = re.compile(pattern)
            match = regex.match(self.codigo, self.posicion)
            if match:
                valor = match.group(0)
                self.posicion = match.end(0)
                if token_type != "ESPACIO":
                    return Token(token_type, valor)
        # Si no coincide con ningún patrón, avanza una posición
        self.posicion += 1
        return None

# Ejemplo de uso
if __name__ == "__main__":
    codigo = '''
    función sumar(a, b) {
        retornar a + b;
    }

    imprimir(sumar(5, 3));
    '''

    lexer = Lexer(codigo)
    tokens = lexer.analizar()
    for token in tokens:
        print(token)

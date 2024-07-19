# src/parser.py

from lexer import Lexer, Token

class ASTNode:
    def __init__(self, tipo, valor=None):
        self.tipo = tipo
        self.valor = valor
        self.hijos = []
    
    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)
    
    def __repr__(self):
        return f"ASTNode({self.tipo}, {self.valor}, hijos={self.hijos})"

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicion = 0
    
    def obtener_token_actual(self):
        if self.posicion < len(self.tokens):
            return self.tokens[self.posicion]
        return None
    
    def avanzar(self):
        self.posicion += 1
    
    def esperar_token(self, tipo):
        token = self.obtener_token_actual()
        if token and token.tipo == tipo:
            self.avanzar()
            return token
        raise SyntaxError(f"Se esperaba un token de tipo {tipo} pero se obtuvo {token}")
    
    def parse(self):
        return self.parse_programa()
    
    def parse_programa(self):
        nodo_programa = ASTNode("PROGRAMA")
        while self.obtener_token_actual() is not None:
            nodo_declaracion = self.parse_declaracion()
            nodo_programa.agregar_hijo(nodo_declaracion)
        return nodo_programa
    
    def parse_declaracion(self):
        token = self.obtener_token_actual()
        if token.tipo == "PALABRA_CLAVE" and token.valor == "función":
            return self.parse_funcion()
        elif token.tipo == "PALABRA_CLAVE" and token.valor == "clase":
            return self.parse_clase()
        else:
            return self.parse_expresion()
    
    def parse_funcion(self):
        self.esperar_token("PALABRA_CLAVE")  # función
        nombre = self.esperar_token("IDENTIFICADOR")
        self.esperar_token("PARENTESIS_IZQUIERDO")
        parametros = self.parse_lista_parametros()
        self.esperar_token("PARENTESIS_DERECHO")
        cuerpo = self.parse_bloque()
        
        nodo_funcion = ASTNode("FUNCION", nombre.valor)
        nodo_funcion.agregar_hijo(parametros)
        nodo_funcion.agregar_hijo(cuerpo)
        return nodo_funcion
    
    def parse_lista_parametros(self):
        nodo_parametros = ASTNode("PARAMETROS")
        while self.obtener_token_actual().tipo != "PARENTESIS_DERECHO":
            parametro = self.esperar_token("IDENTIFICADOR")
            nodo_parametros.agregar_hijo(ASTNode("PARAMETRO", parametro.valor))
            if self.obtener_token_actual().tipo == "COMA":
                self.avanzar()
        return nodo_parametros
    
    def parse_bloque(self):
        self.esperar_token("LLAVE_IZQUIERDA")
        nodo_bloque = ASTNode("BLOQUE")
        while self.obtener_token_actual().tipo != "LLAVE_DERECHA":
            nodo_sentencia = self.parse_declaracion()
            nodo_bloque.agregar_hijo(nodo_sentencia)
        self.esperar_token("LLAVE_DERECHA")
        return nodo_bloque
    
    def parse_clase(self):
        self.esperar_token("PALABRA_CLAVE")  # clase
        nombre = self.esperar_token("IDENTIFICADOR")
        cuerpo = self.parse_bloque()
        
        nodo_clase = ASTNode("CLASE", nombre.valor)
        nodo_clase.agregar_hijo(cuerpo)
        return nodo_clase
    
    def parse_expresion(self):
        # Implementar lógica para parsing de expresiones
        token = self.obtener_token_actual()
        self.avanzar()
        return ASTNode("EXPRESION", token.valor)

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
    parser = Parser(tokens)
    ast = parser.parse()
    print(ast)

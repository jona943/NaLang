### Tipos de Datos en NaLang

`docs/types.md`

```markdown
# Tipos de Datos en NaLang

NaLang soporta varios tipos de datos básicos que son esenciales para la programación. A continuación, se describen los tipos de datos disponibles y cómo se utilizan en NaLang.

## Número

### Entero
Los números enteros son valores numéricos sin parte decimal. Se pueden usar para realizar operaciones aritméticas básicas.

```nalang
entero = 10
```

### Flotante
Los números flotantes son valores numéricos con parte decimal. También se pueden usar en operaciones aritméticas.

```nalang
flotante = 10.5
```

## Texto

### Cadena
Las cadenas son secuencias de caracteres delimitadas por comillas dobles (`"`). Se utilizan para representar texto.

```nalang
cadena = "Hola, mundo"
```

## Booleano

### Valores Booleanos
Los valores booleanos representan verdadero o falso. Se utilizan en expresiones lógicas y condicionales.

```nalang
verdadero = verdadero
falso = falso
```

## Estructuras de Datos

### Lista
Las listas son colecciones ordenadas de elementos que pueden ser de diferentes tipos. Los elementos de una lista se delimitan por corchetes (`[]`) y se separan por comas.

```nalang
lista = [1, 2, 3, "cuatro", 5.0]
```

### Tupla
Las tuplas son colecciones inmutables de elementos, es decir, no se pueden modificar después de su creación. Se delimitan por paréntesis (`()`) y se separan por comas.

```nalang
tupla = (1, 2, 3, "cuatro", 5.0)
```

### Diccionario
Los diccionarios son colecciones de pares clave-valor. Cada clave es única y se utiliza para acceder al valor correspondiente. Los diccionarios se delimitan por llaves (`{}`) y los pares clave-valor se separan por comas, con una clave y un valor separados por dos puntos (`:`).

```nalang
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}
```

## Operaciones con Tipos de Datos

### Operaciones Aritméticas
Se pueden realizar operaciones aritméticas básicas con números.

```nalang
a = 10
b = 5
suma = a + b
resta = a - b
producto = a * b
cociente = a / b
resto = a % b
```

### Concatenación de Cadenas
Las cadenas se pueden concatenar utilizando el operador `+`.

```nalang
saludo = "Hola, "
nombre = "mundo"
mensaje = saludo + nombre  # Resultado: "Hola, mundo"
```

### Acceso a Elementos en Listas y Diccionarios
Se puede acceder a los elementos de una lista o un diccionario utilizando índices y claves, respectivamente.

```nalang
lista = [1, 2, 3, 4, 5]
elemento = lista[2]  # Resultado: 3

diccionario = {
    "nombre": "Juan",
    "edad": 30
}
nombre = diccionario["nombre"]  # Resultado: "Juan"
```

### Modificación de Listas y Diccionarios
Las listas y diccionarios son mutables, lo que significa que se pueden modificar después de su creación.

```nalang
lista = [1, 2, 3]
lista[0] = 10  # La lista ahora es [10, 2, 3]

diccionario = {
    "nombre": "Juan",
    "edad": 30
}
diccionario["edad"] = 31  # El diccionario ahora es {"nombre": "Juan", "edad": 31}
```

### Funciones con Tipos de Datos
Se pueden definir funciones que trabajen con diferentes tipos de datos.

```nalang
función sumar(a, b) {
    retornar a + b
}

resultado = sumar(5, 10)  # Resultado: 15

función saludar(nombre) {
    retornar "Hola, " + nombre
}

mensaje = saludar("Mundo")  # Resultado: "Hola, Mundo"
```

## Conclusión

NaLang proporciona un conjunto básico pero poderoso de tipos de datos que permiten a los usuarios aprender y aplicar conceptos fundamentales de programación. Estos tipos de datos y sus operaciones asociadas forman la base de la mayoría de los programas escritos en NaLang.
```

Este documento proporciona una descripción detallada de los tipos de datos disponibles en NaLang, junto con ejemplos de cómo utilizarlos.
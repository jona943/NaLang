### Sintaxis de NaLang

`docs/syntax.md`

```markdown
# Sintaxis de NaLang

## Introducción

NaLang LP tiene una sintaxis clara y sencilla, diseñada para ser accesible a principiantes y hablantes de español. Este documento describe la sintaxis básica y las estructuras del lenguaje, proporcionando ejemplos para ilustrar su uso.

## Palabras Reservadas

Las siguientes palabras son reservadas en NaLang y no pueden ser utilizadas como identificadores:

```
si, sino, mientras, para, imprimir, verdadero, falso, nulo, y, o, no, función, retornar, clase, hereda
```

## Tipos de Datos

NaLang soporta varios tipos de datos básicos:

- **Número:** `entero` y `flotante`
- **Texto:** `cadena`
- **Booleano:** `verdadero`, `falso`
- **Lista:** Colección ordenada de elementos.
- **Tupla:** Colección inmutable de elementos.
- **Diccionario:** Colección de pares clave-valor.

## Variables y Asignación

Las variables en NaLang se definen y asignan utilizando el operador `=`:

```nalang
variable = 10
nombre = "NaLang"
```

## Comentarios

NaLang soporta comentarios de una sola línea y de varias líneas:

```nalang
# Este es un comentario de una línea

# Comentario
# de varias
# líneas
```

## Operadores

NaLang incluye operadores aritméticos, lógicos y de comparación:

- **Aritméticos:** `+`, `-`, `*`, `/`, `%`
- **Lógicos:** `y`, `o`, `no`
- **Comparación:** `==`, `!=`, `<`, `>`, `<=`, `>=`

## Estructuras de Control

### Condicionales

Las estructuras condicionales permiten la ejecución de código basado en condiciones:

```nalang
si (condición) {
    # Código a ejecutar si la condición es verdadera
} sino {
    # Código a ejecutar si la condición es falsa
}
```

### Bucles

NaLang soporta dos tipos principales de bucles: `mientras` y `para`.

#### Mientras

El bucle `mientras` ejecuta un bloque de código mientras una condición sea verdadera:

```nalang
mientras (condición) {
    # Código a ejecutar mientras la condición sea verdadera
}
```

#### Para

El bucle `para` se utiliza para iterar sobre una secuencia de valores:

```nalang
para (variable en rango(inicio, fin)) {
    # Código a ejecutar para cada valor en el rango
}
```

## Funciones

Las funciones en NaLang se definen utilizando la palabra clave `función` y se pueden invocar por su nombre:

```nalang
función saludar(nombre) {
    imprimir("Hola, " + nombre + "!")
}

saludar("Mundo")
```

### Retorno de Valores

Las funciones pueden devolver valores utilizando la palabra clave `retornar`:

```nalang
función sumar(a, b) {
    retornar a + b
}

resultado = sumar(5, 3)
imprimir(resultado)  # Output: 8
```

## Clases y Objetos

NaLang soporta la programación orientada a objetos. Las clases se definen utilizando la palabra clave `clase` y pueden contener métodos y propiedades:

```nalang
clase Persona {
    función __inicializar__(nombre, edad) {
        self.nombre = nombre
        self.edad = edad
    }

    función presentar() {
        imprimir("Me llamo " + self.nombre + " y tengo " + self.edad + " años.")
    }
}

persona1 = Persona("Juan", 30)
persona1.presentar()
```

## Ejemplos de Código

### Ejemplo 1: Asignación y Operadores

```nalang
a = 5
b = 10
c = a + b
imprimir(c)  # Output: 15

d = verdadero y falso
imprimir(d)  # Output: falso
```

### Ejemplo 2: Condicionales y Bucles

```nalang
si (a > b) {
    imprimir("a es mayor que b")
} sino {
    imprimir("a no es mayor que b")
}

para (i en rango(0, 5)) {
    imprimir(i)
}
```

### Ejemplo 3: Funciones y Estructuras de Datos

```nalang
función sumar(lista) {
    suma = 0
    para (elemento en lista) {
        suma = suma + elemento
    }
    retornar suma
}

mis_numeros = [1, 2, 3, 4, 5]
resultado = sumar(mis_numeros)
imprimir(resultado)  # Output: 15
```

### Ejemplo 4: Clases y Objetos

```nalang
clase Coche {
    función __inicializar__(marca, modelo) {
        self.marca = marca
        self.modelo = modelo
    }

    función mostrar_info() {
        imprimir("Marca: " + self.marca + ", Modelo: " + self.modelo)
    }
}

mi_coche = Coche("Toyota", "Corolla")
mi_coche.mostrar_info()  # Output: Marca: Toyota, Modelo: Corolla
```

Visión completa de la sintaxis de NaLang, permitiendo a los usuarios entender y escribir programas básicos en este lenguaje.
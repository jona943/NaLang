### Ejemplos de Código en NaLang

`docs/examples.md`

```markdown
# Ejemplos de Código en NaLang

A continuación se presentan varios ejemplos de código escritos en NaLang para ilustrar el uso del lenguaje y sus características.

## Ejemplo 1: Asignación y Operadores

Este ejemplo muestra cómo asignar valores a variables y utilizar operadores aritméticos y lógicos.

```nalang
a = 5
b = 10
c = a + b
imprimir(c)  # Output: 15

d = verdadero y falso
imprimir(d)  # Output: falso
```

## Ejemplo 2: Condicionales

Este ejemplo demuestra cómo usar las estructuras condicionales `si` y `sino`.

```nalang
a = 5
b = 10

si (a > b) {
    imprimir("a es mayor que b")
} sino {
    imprimir("a no es mayor que b")
}
```

## Ejemplo 3: Bucles

Este ejemplo ilustra el uso de los bucles `mientras` y `para`.

### Mientras

```nalang
contador = 0

mientras (contador < 5) {
    imprimir(contador)
    contador = contador + 1
}
```

### Para

```nalang
para (i en rango(0, 5)) {
    imprimir(i)
}
```

## Ejemplo 4: Funciones

Este ejemplo muestra cómo definir y utilizar funciones en NaLang.

```nalang
función saludar(nombre) {
    imprimir("Hola, " + nombre + "!")
}

saludar("Mundo")  # Output: Hola, Mundo!
```

### Retorno de Valores

```nalang
función sumar(a, b) {
    retornar a + b
}

resultado = sumar(5, 3)
imprimir(resultado)  # Output: 8
```

## Ejemplo 5: Estructuras de Datos

Este ejemplo ilustra cómo trabajar con listas, tuplas y diccionarios en NaLang.

### Listas

```nalang
mi_lista = [1, 2, 3, 4, 5]
imprimir(mi_lista[2])  # Output: 3

mi_lista[2] = 10
imprimir(mi_lista)  # Output: [1, 2, 10, 4, 5]
```

### Tuplas

```nalang
mi_tupla = (1, 2, 3, 4, 5)
imprimir(mi_tupla[2])  # Output: 3

# Las tuplas son inmutables, no se pueden modificar
```

### Diccionarios

```nalang
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30
}

imprimir(mi_diccionario["nombre"])  # Output: Juan

mi_diccionario["edad"] = 31
imprimir(mi_diccionario)  # Output: {"nombre": "Juan", "edad": 31}
```

## Ejemplo 6: Clases y Objetos

Este ejemplo muestra cómo definir clases y crear objetos en NaLang.

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
persona1.presentar()  # Output: Me llamo Juan y tengo 30 años.
```

## Ejemplo 7: Combinación de Funciones y Estructuras de Datos

Este ejemplo muestra una función que suma los elementos de una lista y devuelve el resultado.

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

Estos ejemplos proporcionan una visión general de cómo utilizar NaLang para escribir programas simples y efectivos. Cada ejemplo demuestra una característica clave del lenguaje, ayudando a los usuarios a familiarizarse con su sintaxis y funcionalidad.
```
---
author: Mindusting
corrected: true
tags:
  - Programming/Python/DataStructure
title: Tuplas en Python
rating: 1
---

# TUPLAS EN PYTHON

> [!help]- REFERENCIAS WEB
> - [W3 (Tuple)](https://www.w3schools.com/python/python_tuples.asp)

Una **Tupla** es una estructura de datos [inmutable](py_inmutable.md), esto lo que quiere decir es que una vez es declarada esta no se puede modificar.

Para declarar una **Tupla** se debe ==separar una secuencia de valores con *comas*== (`,`); ==los paréntesis no son necesarios==, esto es algo con lo que se confunde mucha gente, los paréntesis (`()`) no son los que indican la creación de la **Tupla**, sino las *comas* (`,`):

```py
x = 3,
y = (2)

print(type(x))
print(type(y))
# SALIDA:
# <class 'tuple'>
# <class 'int'>
```

Esto implica que si queremos pasar una **Tupla** con un único elemento como argumento como podría ocurrir en la inserción a una [base de datos](../db/db.md) con [SQLite3](sqlite3/py_sqlite3.md), tendremos que hacerlo de la siguiente forma (*Este caso es un poco complicado si eres nuevo, por lo que si ese es tu caso, mejor ve al [siguiente apartado](#ACCESO%20A%20ELEMENTOS)*):

```py
import sqlite3

cx = sqlite3.connect("main.db")
cr = cx.cursor()

cr.execute(
    "INSERT INTO users (name) VALUES (?);",
    ("Adelio",) # <- Se crea una tupla de un elemento.
)

cx.commit()

cr.close()
cx.close()
```

---

Si queremos crear una **Tupla** a partir de otro iterable, podemos hacerlo mediante la [clase](py_class.md) `tuple`; esta recibe un único argumento, siendo este el iterable a original.

> [!abstract] SINTAXIS
> tuple(***\[iterable\]***)

```py
l = [3, 2, 5]
t = tuple(l)

print(l)
print(t)
print(type(l))
print(type(t))
# SALIDA:
# [3, 2, 5]
# (3, 2, 5)
# <class 'list'>
# <class 'tuple'>
```

## ACCESO A ELEMENTOS

Si tenemos una **Tupla** y queremos obtener uno de sus elementos podemos hacerlo mediante su índice, esto es un [`int`](py_int.md) que identifica de forma única a cada elemento de la **Tupla**, empezando por el cero y subiendo consecutivamente hasta poder identificar todos los elementos; también existe la posibilidad de indicar un número negativo, pudiendo así ir contando desde el fin hacia el inicio de la **Tupla**:

> [!note] NOTA
> Si quieres saber cómo funciona el índice en las **Tuplas** te recomiendo que leas la documentación a cerca de los [Arrays en programación](../pc/pc_array.md), concretamente el apartado [básico](../pc/pc_array.md#BÁSICO); aunque un **Array** no es lo mismo que una **Tupla** el cómo funciona el índice es muy parecido por no decir igual.

> [!abstract] SINTAXIS
> ***\[tupleName\]***\[***\[index\]***\]

```py
t = (3, 2, 5)

print(t[0])
print(t[1])
print(t[2])
# SALIDA:
# 3
# 2
# 5

print(t[-1])
print(t[-2])
print(t[-3])
# SALIDA:
# 5
# 2
# 3
```

---

Cabe resaltar que el índice no es necesario especificarlo a pelo en el código, sino que con que le ofrezcamos una [`int`](py_int.md) funcionará perfectamente.

```py
t = (3, 2, 5)

index = int(input("Introduce un entero entre -3 y 2: "))

print(t[index])
```

---

Es posible que te estés preguntando qué pasaría si introduces un índice que no está dentro del rango de posibilidades de la **Tupla**; lo que ocurre es que se lanza una [excepción](py_exceptions.md) de tipo `IndexError`, indicado así que nos hemos salido de los límites; ésta, por supuesto se puede atrapar con un [control de excepciones](py_exceptions.md#CONTROL%20DE%20EXCEPCIONES).

```py
try:
    t = (3, 2, 5)
    
    index = int(input("Introduce un entero entre -3 y 2: "))
    
    print(t[index])

except ValueError:
    print("No has introducido un número.")

except IndexError:
    print("El índice está fuera del rango.")
```

## MÉTODOS

Las **Tuplas** contienen varios [métodos](class/py_methods.md) que permiten trabajar sobre ellas de una forma más sencilla.

### MÉTODO COUNT

El método `count` recibe un único argumento con el valor; este se buscará a lo largo de toda la **tupla** y devolverá el número de veces que lo haya encontrado en forma de [`int`](py_int.md).

> [!abstract] SINTAXIS
> count(***\[value\]***) -> int

```py
t = (3, 2, 5, 3)
v = 3

# Se cuenta el número de ocurrencias.
n = t.count(v)

print(f"En la tupla hay {n} veces el valor {v}.")
# SALIDA:
# En la tupla hay 2 veces el valor 3.
```

### MÉTODO INDEX

El método `index` sirve para obtener el índice de un elemento que estemos buscando dentro de la **Tupla**; puede recibir hasta tres argumentos de los cuales el primero es obligatorio; el primer argumento indica cual es el valor del cual queremos obtener el índice, el segundo es un [`int`](py_int.md) que indica desde qué índice queremos empezar a buscar (*siendo el valor por defecto `0`*), el tercer argumento es un [`int`](py_int.md) que indica hasta donde queremos buscar (*siendo el valor por defecto `2^63-1`*).

Si dentro del rango de índices indicado no se encuentra ninguna ocurrencia del valor a buscar, se lanzará una [excepción](py_exceptions.md) de tipo `ValueError`.

> [!abstract] SINTAXIS
> index(***\[value\]***, ***\[start\]***, ***\[end\]***)

```py
t = (3, 2, 5, 3)
v = 3

try:
    # Se busca la primera ocurrencia.
    i = t.index(v)
    
    print(f"Se ha encontrado el valor {v} en el índice {i}.")
    # SALIDA:
    # Se ha encontrado el valor 3 en el índice 0.
except ValueError:
    # Esta parte del código se ejecuta cuando
    # se lanza la excepción ValueError debido 
    # a que no se ha encontrado el valor.

    print(f"No se encontró ningún {v} en la tupla.")
```

## MÉTODOS PROPIOS

> [!info]- VE TAMBIÉN
> - [Contador de valores](py_dict.md#CONTADOR%20DE%20VALORES)

### ÍNDICES DE VALORES

```py
def value_indexes(arr: list | tuple, value) -> list:
    res: list = list()
    start: int = 0

    try:
        while True:
            start = arr.index(value, start)
            res.append(start)
            start += 1
    except ValueError:
        # Simplemente termina el proceso.
        pass

    return res


t = (3, 2, 5, 3)
print(value_indexes(t))
# SALIDA:
# [0, 3]
```

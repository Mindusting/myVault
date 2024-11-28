---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/NumPy
title: Módulo NumPy en Python
---

<h1 style="text-align:center;">NUMPY</h1>

---

# DOCUMENTACIÓN WEB

- [Documentación oficial de NumPy](https://numpy.org/doc/stable/reference/arrays.html)
- [NumPy en W3](https://www.w3schools.com/python/numpy/default.asp)

# NUMPY

El [módulo](../py_module.md)

```python
import numpy as np
import os

clear = lambda: os.system("cls" if "nt" == os.name else "clear")

clear()

arr: list = list()

arr.append(np.array([[65, 66, 67], [68, 69, 70]], dtype=np.uint8))
arr.append(np.array(["Hola", "Mundo"], dtype=str))

with open("save.npy", "wb") as file:
    np.save(file, arr[0])
    np.save(file, arr[1])

del arr
arr: list = list()

with open("save.npy", "rb") as file:
    arr.append(np.load(file))
    arr.append(np.load(file))

for element in arr:
    print(element)
```

```python
import numpy as np

arr = np.array(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
)
print(arr[0, :])
print(arr[:, 0])
# SALIDA:
# [1 2 3]
# [1 4 7]

"""
En el primer caso se está escogiendo el primer elemento del array y después se indica que se quiere todos.

En el segundo caso, selecciona todos los elementos del array y luego de estos, escoge el primer elemento de cada uno.
"""

print("-" * 10)

print(arr[0][:])
print(arr[:][0])
# SALIDA:
# [1 2 3]
# [1 2 3]
"""
En el primer caso se está escogiendo el primer elemento del array y después, de ese nuevo array se escoge todos los elementos.

En el segundo caso, selecciona todos los elementos del array y luego, de ese nuevo array se escoge el primero.
"""
```

```python
import numpy as np

x = np.eye(3, dtype=np.int8)
y = np.ones((3, 3), dtype=np.int8)
np.save('arr.npy', x)
np.savetxt('arr.txt', x)
np.savez('arr.npz', x, y)

"""
Esto permite guardar el contenido de los arrays en archivos.
"""
```

%%
# NUMPY

>[!fail] ESTE APARTADO ESTÁ INCOMPLETO

<https://www.w3schools.com/python/numpy/numpy_intro.asp>
[Python Simplified](https://youtu.be/lLRBYKwP8GQ)

NumPy en una librería especializada en los array(s) y matrices, permitiendo manejar grandes elementos de este tipo de una forma eficiente y rápida, ya que son de tipazo fuerte y ofrece múltiples métodos especializado en el manejo de matrizes, simplificando mucho su uso.

>[!info]
>Para instalar *numpy* se usa el comando "***pip install numpy***".

Una vez esté instalado NumPy para poder usarlo en nuestro proyecto tendremos que importarlo, por lo general se suele renombrar a `np` para que sea más sencillo de escribir.

>[!quote] Así es como se suele importar el módulo `numpy`:
>```python
>import numpy as np
>```

## ARRAY

Un array es similar a las listas [lista](<##LISTAS>), con la diferencia que estas, no se les puede cambiar el tamaño y es de [tipado fuerte](../../09-PC/PC.md##%20TIPO%20DE%20TIPADO TIPO DE TIPADO>), por lo que es más estricta que las [listas](<##LISTAS>), pero son más rápidas y eficientes.

La forma de localizar un valor dentro de un array es mediante el índice el elemento, al igual que ocurre conlas [listas](<##LISTAS>), este índice puede ser tanto positivo como negativo, funcionando de la misma forma.

>[!note] Así sería el índice normal e inverso:
>Este es un array con los valores *\[5,3,7\]*.
>
>|    INDEX    |    0   |    1   |    2   |
>|:-----------:|:------:|:------:|:------:|
>|    VALUE    |    5   |    3   |    7   |
>| **INV-INX** | **-3** | **-2** | **-1** |

Para empezar vamos a ver como crear nuestro primer array de forma sencilla y vamos a ver unos ejemplos de como se manipula, luego veremos en los próximos apartados más en detalle el las diferentes funciones que tiene.

Para crear un array de tres elementos y visualizar el contenido podemos hacer lo siguiente:

>[!example] Ej. como crear nuestro primer array:
>```python
>import numpy as np
>
>arr = np.zeros(3, dtype=np.uint8)
>
>print(arr)
># SALIDA:
># [0 0 0]
>```
>En este ejemplo podemos ver como llamamos al módulo `numpy` con el nombre de `np` seguido a este indicamos que queremos acceder al método estático `zeros`, este permite crear un array lleno de ceros, el primer argumento que le indicamos es el tamaño de la [dimensión](<## MATRICES>) (*Esto de las dimensiones lo veremos más a fondo en un próximo apartado.*), seguido por el tipo de dato que se va a almacenar (*Este ultimo no es necesario, pero es recomendable indicarlo, más adelante se explicará más a fondo que tipos existen*), en teste caso es un valor entero de **ocho bits sin signo** (***uint8 = Unsigned-INTeger-8bit***), por lo que el valores que podrá almacenar estarán serán números enteros igual o mayor que `0` y menor a `256`.

>[!example] Ej. de asignación de valores al array:
>```python
>import numpy as np
>
>arr = np.zeros(3, dtype=np.uint8)
>
>arr[0] = 5
>arr[1] = 3.141592
>arr[2] = True
>
>print(arr)
># SALIDA:
># [5 3 1]
>```
>En este ejemplo se asigna a los tres elementos del array diferentes valores, si te fijas los valores indicados no son lo que se han guardado, por ejemplo el número PI ha sido guardado como `3` y el valor `True` se ha guardado como `1` esto es debido a que este array al ser de tipo `uint8` solo puede guardar valores enteros (*igual o mayor que `0` y menor a `256`*), es por esto que a los valores decimales les quita la parte decimal y los valores booleanos los interpreta como `1` o `0`.
>
>---
>
>Otra forma de asignar valores es mediante rangos de índices:
>
>```python
>import numpy as np
>
>arr = np.zeros(3, dtype=np.uint8)
>
>arr[:] = 9
>print(arr)
># SALIDA:
># [9 9 9]
>
>arr[1:] = 3
>print(arr)
># SALIDA:
># [9 3 3]
>```
>En este ejemplo se puede ver como se le asigna a todos los elementos del array a `9` y luego se le asigna a todos los elementos con índice igual o mayor a `1` el valor de `3`.
>
>---
>
>Otra forma de asignar valores es a través de un condicional:
>
>```python
>import numpy as np
>
>arr = np.zeros(3, dtype=np.uint8)
>
>arr[0] = 9
>arr[1:] = 3
>print(arr)
># SALIDA:
># [9 3 3]
>
>arr[arr == 3] = 6
>print(arr)
># SALIDA:
># [9 6 6]
>```
>En este ejemplo se puede ver como primero al array es `[9 3 3]` y después se le asigna a todos los elementos con valor igual a `3` los asigne a `6`, acabando con el resultado `[9 6 6]`.

## TIPOS DE DATOS

>[!fail] ESTE APARTADO ESTÁ INCOMPLETO

Para asignar un tipo de dato a un array se hace a través del argumento `dtype`, a este se le puede asignar diferentes tipos de datos:

Enteros:

- Integer:
    - Signed:
        - int8
        - int16
        - int32
        - int64
    - Unsigned:
        - uint8
        - uint16
        - uint32
        - uint64
- float
    - float16
    - float32
    - float64
- str_
- bool_

```python
from Terminal import clear
import numpy as np

clear()

arr = np.zeros((3), dtype=np.float16)

arr[0] = 3.1415926535

print(arr)
print(arr.dtype)

np.int8
np.int16
np.int32
np.int64

np.uint8
np.uint16
np.uint32
np.uint64

np.float16
np.float32
np.float64

np.str_("<U8")

np.bool_
```

## ARRAY DE TIPO RANGO

Para crear un array con una secuencia de valores se usa el método `np.arange()` (***arange = Array-RANGE***), esta funciona de una forma similar a la clase `range()`, con la diferencia que el argumento `step` permite números decimales.

>[!example] Ej. de uso del método estático `arange()`:
>```python
>import numpy as np
>
>arr = np.arange(3)
>print(f"Array 1: {arr}")
># SALIDA:
># Array 1: [0 1 2]
>
>arr = np.arange(3, 6)
>print(f"Array 2: {arr}")
># SALIDA:
># Array 2: [3 4 5]
>
>arr = np.arange(6, 9, 0.5)
>print(f"Array 3: {arr}")
># SALIDA:
># Array 3: [6.  6.5 7.  7.5 8.  8.5]
>```

## TRANSFORMAR LISTAS Y TUPLAS A ARRAY(S)

Para trasformar una [lista](<##LISTAS>) o [tupla](<##TUPLAS 📃>) en un array se hace usando el método `np.array()`, este puede recibir como argumento de forma directa la [lista](<##LISTAS>) o [tupla](<##TUPLAS 📃>), o se puede indicar con a través del nombre de la [lista](<##LISTAS>) o [tupla](<##TUPLAS 📃>).

```python
arr = np.array([5, 2, 3])
print(arr)

my_list = [5, 2, 3]
arr = np.array(my_list)
print(arr)
```

Los array(s) son de tipado fuerte, por lo qué si en la [lista](<##LISTAS>) o [tupla](<##TUPLAS 📃>) tenemos elementos de diferentes tipos, el array será del tipo com mayor prioridad según la siguiente lista.

1. String.
2. Float.
3. Integer.
4. Boolean.

Esta lista indica que si dentro de la [lista](<##LISTAS>) o [tupla](<##TUPLAS 📃>) nos encontramos con un valor de tipo `String` el array, será de este tipo, por lo que transformará el resto de valores a este, si no se encuentra ninguno aplicará la misma lógina con el resto de valores, y así hasta llegar al final de la lista.

Luego también tendremos que tener en cuenta que dentro de cada tipo de estos podremos encontrar diferentes rangos de valores, como puede ser `np.int32` (*entero de 32 bits*) o `np.int64` (*entero de 64 bits*).

## MATRICES

Una matriz no es más que un array multidimensional, esto se puede enteder mejor con un ejemplo.

| INDEX | 0 | 1 | 2 |
|:-----:|:-:|:-:|:-:|
| VALUE | 5 | 3 | 7 |

| INVERS-INDEX | -3 | -2 | -1 |
|:------------:|:--:|:--:|:--:|
|     VALUE    |  5 |  3 |  7 |

|       INDEX      |    0   |    1   |    2   |
|:----------------:|:------:|:------:|:------:|
|       VALUE      |    5   |    3   |    7   |
| **INVERS-INDEX** | **-3** | **-2** | **-1** |

|       INDEX      |    0   |    1   |    2   |
|:----------------:|:------:|:------:|:------:|
| **INVERS-INDEX** | **-3** | **-2** | **-1** |
|       VALUE      |    5   |    3   |    7   |

| INDEX | VALUE | INVERS-INDEX |
|:-----:|:-----:|:------------:|
|   0   |   5   |      -1      |
|   1   |   3   |      -2      |
|   2   |   7   |      -3      |

| INDEX | X | 0 | 1 | 2 |
|:-----:|:-:|:-:|:-:|:-:|
| **Y** | + |\| |\| |\| |
| **0** | - | 1 | 2 | 3 |
| **1** | - | 4 | 5 | 6 |
| **2** | - | 7 | 8 | 9 |

```python
import numpy as np

size = 7

arr = np.zeros((size, size), dtype=np.uint8)

arr[1:3, 1:3] = 1
arr[1:3, -3:-1] = 2
arr[-3:-1, 1:3] = 3
arr[-3:-1, -3:-1] = 4

print(arr)
# SALIDA:
# [[0 0 0 0 0 0 0]
#  [0 1 1 0 2 2 0]
#  [0 1 1 0 2 2 0]
#  [0 0 0 0 0 0 0]
#  [0 3 3 0 4 4 0]
#  [0 3 3 0 4 4 0]
#  [0 0 0 0 0 0 0]]
```

---

## TIPOS DE VALORES

Tipos de datos en NumPy:

```python
import numpy as np

np.int8
np.int16
np.int32
np.int64

np.float16
np.float32
np.float64
```

Array(s) multidemensionales

```python
arr = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int8)

arr = arr.reshape(4, 2)
arr = arr.reshape(8)
arr = arr.reshape(2, 2, 2)

print(arr)
print(arr.dtype)
print(arr.shape)
```

## OTAS FUNCIONES

```python
import numpy as np

#'''
# Podemos crear un array
# con todo ceros.
arr = np.zeros([2, 2])

# Podemos crear un array
# con todo unos.
arr = np.ones([2, 2])

# Podemos crear un array con
# números inconsistentes.
arr = np.empty([2, 2])

# Podemos crear un línea
# diagonal de unos
# en un array llenos de ceros. 
arr = np.eye(3)

# Podemos hacer que esta
# línea se desplace
# hacia el noreste indicando
# el parámetro "k" con
# el número de pasos a desplazarse.
arr = np.eye(3, k=1)

# Si el valor de "K" es negatívo, esta
# línea se desplazará en dirección
# sureste.
arr = np.eye(3, k=-1)

# Podemos indicar un filtro.
# este se compone por un condicional,
# si este se cumple, asignará el
# nievo valor al elemento.
arr[arr == 1] = 10

# Podemos asignar un valor nuevo
# a un área del array.
arr[-2:] = 3
arr[:, -1] = 2

# Ordena los elementos del eje X
# de menor a mayor.
arr = np.sort(arr)

# Podemos indicar que se ordene
# en el eje Y escribiendo el argumento
# "asix" ("Eje" en inglés) con el
# valor de 0, siendo el X = -1 (este
# es el por defecto).
arr = np.sort(arr, axis=0)

## TIPOS DE ALGORITMOS PARA ORDENAR
# Si quisieramos cambiar el tipo de
# algoritmo que se va a usar a la
# hora de ordenar los valores, es
# puede hacer mediante el argumento
# "kind" ("Tipo" en inglés), y este
# podrá tener los valores:
# - "mergesort".
# - "heapsort".

print(arr)
#'''
```

```python
import numpy as np


arr = np.array([
    [0,0,0],
    [0,0,0],
    [0,0,0]
], dtype=np.int8)


print("Array:")
print(arr)
# Número de dimensiones
print(f"Dimensions: {arr.ndim}")
# Forma del Array
print(f"Shape: {arr.shape}")
# Número de elementos
print(f"Size: {arr.size}")
# Tipo de valor a guardar
print(f"Type: {arr.dtype}")
# Número de bytes por elemento
print(f"Bytes: {arr.itemsize}")
# Número de bytes total
print(f"N-Bytes: {arr.nbytes}")
```

El método `sum` permite sumar todos los valores de la matriz en el eje que indiquemos.

Para copiar un array se usa el método `copy`, por qué si no, lo que hara será copiar la dirección en memoria, probocando que si modificas la copia también cambie la original.
```python
import numpy as py

arr = np.array([1,2,3])

arrCopy = arr.copy()

arr[0] = 9

print(arr)
print()
print(arrCopy)
```

## ARRAY(S) Y MATRICES

### CEROS

Crea un array llenos de ceros.

`np.zeros(3)`
`np.zeros(2, 2)`

### UNOS

Crea un array lleno de unos.

`np.ones(3)`
`np.ones(2, 2)`

```python
import time
import os

clear = lambda: os.system("cls" if "nt" == os.name else "clear")
overwrite = lambda: print("\033[H\033[2J", end="")

import numpy as np

size = 8

arr = np.random.random((size,size))

arr = arr * 255
arr = np.array(arr, dtype=np.uint8)

print(arr)

print()
arr = np.array2string(arr, formatter={"int":lambda x: f"{hex(x)[2:].upper():02}"})#f"{str(hex(x))}"})

print(arr)
#print(type(arr[0]))
#print(arr.dtype)
```
%%

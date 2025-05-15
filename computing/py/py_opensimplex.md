---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/OpenSimplex
title: Módulo OpenSimplex en Python
---

# SIMPLEX NOISE

El *simplex noise* es el resultado de una operación matemática en la cual si versión más simple permite crear una matriz de número que a primera vista **podrían parecer aleatorios** y entre ellos están relacionados.

A continuación veremos un ejemplo representado con caracteres `ascii` de la matriz de *simplex noise*:

%%
```python
import numpy as np
import opensimplex as ops

size:  int   = 32
start: int   = 0
end:   int   = 4
step:  float = (end - start) / size

arr:    np.ndarray = np.arange(start, end, step) + step
matrix: np.ndarray = ops.noise2array(arr, arr)

chars: tuple = (" ", "░", "▒", "█")
chars: tuple = (" ", ".", ";", "?", "O", "@", "■")

matrix: np.ndarray = abs(matrix)
matrix: np.ndarray = matrix + abs(matrix.min())
matrix: np.ndarray = matrix / matrix.max()
matrix: np.ndarray = matrix * (len(chars) -1)
matrix: np.ndarray = matrix.round()
matrix: np.ndarray = matrix.astype(np.int32)


print("┌", "─" * ((size * 2) + 2), "┐", sep="")

for y_i in range(size):
    print("│ ", end="")
    for x_i in range(size):
        print(chars[matrix[x_i, y_i]] * 2, end="")
    print(" │")

print("└", "─" * ((size * 2) + 2), "┘", sep="")
```
%%

```txt
┌──────────────────────────────────────────────────────────────────┐
│ ??;;............;;??OO@@@@@@@@@@@@OOOOOOOOOO@@@@@@@@@@OO????;;;; │
│ ??;;;;..........;;??OOOO@@@@@@@@@@OOOOOO@@@@@@■■■■@@@@OOOO??;;;; │
│ ??;;;;..........;;;;??OO@@@@@@@@@@OOOOOO@@@@@@@@@@@@@@OOOOOO???? │
│ ??;;;;..........;;;;??OOOO@@@@@@OOOOOOOOOO@@@@@@@@@@@@@@@@OOOO?? │
│ ??;;;;;;;;......;;;;????OOOOOOOOOO??????OOOOOOOO@@@@@@@@@@@@OOOO │
│ ;;;;;;;;;;;;;;;;;;;;;;????OOOO????????????????OOOO@@@@@@@@@@@@OO │
│ ;;;;;;;;????;;;;;;;;;;;;??????????;;;;;;;;;;????OOOO@@@@@@@@@@OO │
│ ;;;;;;??????????;;;;;;;;;;??????;;;;;;..;;;;;;????OO@@@@@@@@@@OO │
│ ;;;;????OOOOOO??;;;;;;;;;;;;????;;;;;;....;;;;????OO@@@@@@@@@@OO │
│ ;;;;??OOOOOOOO????;;;;;;;;;;??????;;;;;;;;;;;;??OOOO@@@@@@@@OO?? │
│ ;;;;??OO@@@@OOOO??;;;;;;;;;;????????????;;??????OO@@@@@@@@@@OO?? │
│ ;;??OOOO@@@@OOOO??;;..;;;;????OOOOOOOO??????OOOO@@@@@@■■@@@@OO?? │
│ ;;??OO@@@@@@OO????;;;;;;;;??OOOO@@@@OOOOOOOOOOOO@@@@■■■■@@@@OOOO │
│ ????OO@@@@@@OO??;;;;;;;;????OO@@@@@@@@OOOOOOOO@@@@@@@@@@@@@@OOOO │
│ ??OOOO@@@@@@OO??;;;;;;;;??OOOO@@@@@@@@OOOOOOOOOO@@@@@@@@@@@@@@@@ │
│ OOOO@@@@@@@@OO??;;;;;;;;??OO@@@@@@@@OOOOOO????OOOOOOOO@@@@@@@@@@ │
│ OO@@@@@@@@OOOO??;;;;;;????OO@@@@@@@@OO??????????????OOOO@@@@@@@@ │
│ @@@@@@@@@@OO????;;;;;;??OOOO@@@@@@OOOO??;;;;;;;;;;????OOOO@@@@@@ │
│ @@■■@@@@@@OO??;;;;;;;;??OO@@@@@@@@OO??;;;;......;;;;;;??OO@@@@@@ │
│ ■■■■■■@@OOOO??;;;;;;????OO@@@@@@OOOO??;;............;;;;??OO@@@@ │
│ ■■■■@@@@OO????;;;;;;????OO@@@@@@OO??;;;;....      ....;;????OOOO │
│ ■■■■@@@@OO??;;;;;;;;??OOOO@@@@@@OO??;;....          ....;;??OOOO │
│ ■■■■@@OOOO??;;;;;;;;??OO@@@@@@OOOO??;;....          ....;;?????? │
│ ■■@@@@OO??;;;;..;;;;??OO@@@@@@OO??;;;;....          ....;;;;???? │
│ ■■@@@@OO??;;;;..;;;;??OOOO@@OOOO??;;......      ........;;;;???? │
│ ■■@@@@OO????;;;;;;;;??OOOOOOOO????;;................;;;;;;?????? │
│ ■■@@@@OOOO??;;;;;;;;????OOOOOO??;;;;............;;;;;;??????OOOO │
│ ■■■■@@@@OO????;;;;;;;;??????????;;;;..........;;;;????OOOOOOOOOO │
│ @@■■■■@@OOOO??;;;;;;;;;;;;;;??;;;;;;........;;;;??OOOOOO@@@@@@OO │
│ @@■■■■@@@@OOOO??;;;;;;;;;;;;;;;;;;;;;;....;;;;????OO@@@@@@@@@@@@ │
│ @@■■■■■■@@@@OO??;;;;....;;;;;;????;;;;;;;;;;;;????OO@@@@■■■■@@@@ │
│ @@@@■■■■■■@@OOOO??;;;;..;;;;????????;;;;;;;;;;;;??OO@@■■■■■■■■@@ │
└──────────────────────────────────────────────────────────────────┘
```

Se a usado los valores obtenidos para crear un mapa de valores en forma de matriz, si modificamos los valores mediante funciones podemos conseguir patrones distintos con el mismo mapa de valores:

```txt
┌──────────────────────────────────────────────────────────────────┐
│ ..;;OOOO@@@@OO??;;  ..;;OOOOOOOO??;;....;;;;??OOOOOO??;;  ..;;?? │
│   ;;??OO@@@@OOOO;;....;;??OOOOOO??;;;;;;;;??OOOOOOOO??;;..  ..;; │
│   ;;??OOOO@@OOOO??..  ;;??OOOO????;;;;;;????OOOOOOOO??;;....  .. │
│   ..;;??OOOOOOOO??;;....;;??????;;;;....;;??????OOOO????;;;;..   │
│ ..;;;;????OOOOOO??;;..  ..;;;;;;..      ....;;;;????OOOO????;;.. │
│ ;;;;;;;;;;????????;;;;..  ....    ........    ..;;????OOOOOO??;; │
│ ;;;;;;......;;;;;;;;;;....    ....;;;;;;;;;;..  ..;;??OOOOOO??;; │
│ ??;;....      ..;;;;??;;........;;;;????????;;..  ;;??OOOOOO??;; │
│ ??;;..  ......  ..;;????;;......;;;;????????;;..  ;;??OOOO??;;.. │
│ ??;;  ..;;;;;;  ..;;????;;;;........;;????;;;;....;;??OOOO??;;   │
│ ??..  ;;????;;....;;????;;..        ..........  ;;??OOOOOO??;;   │
│ ;;....;;????;;....;;????;;..  ..;;....      ..;;??OOOOOOOO??;;   │
│ ..  ..??????;;....??????;;  ..;;????;;;;....;;;;??OOOOOOOO??;;.. │
│ ....;;??????;;  ..????;;..  ;;????????;;;;;;;;????OOOOOOOO??;;.. │
│   ..;;??????;;  ;;????;;....;;??OOOO??;;......;;??????OOOO????;; │
│ ..;;????????..  ;;;;;;..  ..??OOOO??;;....    ....;;;;????OOOO?? │
│ ;;????OO??;;....;;;;;;....;;??OO????;;  ........    ..;;????OOOO │
│ ??OOOOOO??;;  ..;;;;;;  ..;;??OO??;;....;;????;;;;..  ..;;??OOOO │
│ OOOOOOOO??..  ..;;;;..  ..????????..  ;;??OOOOOO??;;;;  ..??OOOO │
│ @@@@OO??;;....;;;;;;..  ;;??????;;....??OOOO@@@@OOOO??..  ;;???? │
│ @@@@OO??;;  ..;;??;;..  ;;??????;;  ;;??OO@@@@@@@@@@OO??....;;;; │
│ @@@@OO??..  ;;????;;....;;??????..  ;;??OO@@■■■■■■@@@@OO;;...... │
│ @@OO??;;....;;????;;....??????;;....;;OO@@@@■■■■■■■■@@OO??..  .. │
│ @@OO??;;  ..??????;;  ..??????;;  ..??OO@@@@■■■■■■@@@@OO??;;..   │
│ OOOO??;;  ..??????;;  ..;;??;;..  ;;??OO@@@@@@@@@@@@OO??;;....   │
│ OOOO??;;  ..;;????;;....;;;;;;  ..;;OOOO@@@@@@OOOO????;;;;..     │
│ OOOO??;;....;;????;;..  ......  ;;??OOOO@@@@OO????;;;;..    .... │
│ OOOOOO??..  ..;;;;;;;;....    ..;;??OOOOOOOO??;;....  ....;;;;;; │
│ OO@@OOOO;;..  ..;;????;;;;......;;????OOOO????..  ....;;??????;; │
│ OO@@@@OO??;;....;;????????;;;;..;;;;????????;;..  ..????OOOO???? │
│ OOOO@@@@OO??..  ..????OO??;;;;....;;;;??????;;..  ;;??OO@@@@OO?? │
│ ??OO@@@@OO??;;....;;??????;;..    ..;;;;????;;..  ;;??@@@@@@@@?? │
└──────────────────────────────────────────────────────────────────┘
```

# RUIDO SIMPLEX

> [!info] INFO
> El *ruido simplex* es una versión mejorada del *ruido de Perlin*, ya que en este último, en ocasiones se podían encontrar patrones en el ruido, por tanto, son bastante parecidos pero **no iguales**.

Para poder calcular el ruido simple tendremos que importar el [módulo](py_module.md) `opensimplex`:

```python
import opensimplex as ops
```

## FUNCIONES

### OBTENER SEMILLA

La [función](py_function.md) `get_seed` devuelve un valor de tipo [`int`](py_int.md) indicando la semilla (*seed*) del *simplex noise*, la semilla es el número que se utiliza para generar el ruido.

```python
import opensimplex as ops

print(ops.get_seed())
# SALIDA:
# 3
```

### SEMILLA ALEATORIA

La [función](py_function.md) `random_seed` establece como semilla (*seed*) del *simplex noise* como un número de tipo [`int`](py_int.md) """aleatorio""", y lo pongo entre comillas ya que si vemos el código de esta [función](py_function.md) podemos ver que el número lo saca de la [función](py_function.md) [`time_ns`](py_time.md) del [módulo](py_module.md) [`time`](py_time.md).

```python
import opensimplex as ops

ops.random_seed()

print(ops.get_seed())
```

En este ejemplo se hace uso de la [función](py_function.md) [`get_seed`](#OBTENER%20SEMILLA) para poder ver que la semilla sí a cambiado.

### ESTABLECER SEMILLA

La [función](py_function.md) `seed` requiere de un argumento de tipo [`int`](py_int.md), este será la semilla (*seed*) que se usará para hacer el *simplex noise*.

```python
import opensimplex as ops

ops.seed(64)

print(ops.get_seed())
# SALIDA:
# 64
```

En este ejemplo se hace uso de la [función](py_function.md) [`get_seed`](#OBTENER%20SEMILLA) para poder ver que la semilla sí a cambiado.

### RUIDO 2D

La [función](py_function.md) `noise2` requiere de dos argumentos, estos pueden ser tanto de tipo [`int`](py_int.md) como [`float`](py_float.md) e indican las coordenadas del del valor que queremos del *simplex noise*.

```python
import opensimplex as ops

ops.seed(64)

print(ops.noise2(0.1, 0.8))
# SALIDA:
# -0.21570461975214264
```

### ARRAY DE RUIDO 2D

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

## NORMALIZACIÓN

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar que es la normalización.
> > - [ ] Explicar como lo he hecho.

```python
# 2D
 0.8643664405098959
-0.8643664405098959

# 3D
 0.9409240383318559
-0.9409240383318558
```

```python
import numpy as np
import opensimplex as opx

MAX_2D_NOISE: float = 0.8643664405098959

array:  np.ndarray = np.arange(0, 10, 0.1)
matrix: np.ndarray = opx.noise2array(array, array)

matrix += MAX_2D_NOISE
matrix *= 1 / (MAX_2D_NOISE * 2)

print(matrix.max())
print(matrix.min())
```

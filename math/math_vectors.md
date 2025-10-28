---
author: Mindusting
corrected: false
tags:
  - Math/Vector
title: Vectores
---

# VECTORES

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> YouTube:
> - [3Blue1Brown (Essence of linear algebra)](https://youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&si=9YzrArg_yeN4oTzZ)
> - [El traductor de ingeniería (Vectors)](https://youtu.be/eXA4806YuqY)

Los vectores se componen de tres atributos:

- *Módulo*: representa la longitud del **vector**, siendo proporcional a la *magnitud*.
- *Dirección*: es la misma sobre la recta en la que se posa.
- *Sentido*: es representado por la flecha en uno de los extremos del **vector**.

> [!example] Ejemplo de vector:
> ![#center](excalidraw/math_vector_f10.md)
> - El *módulo* o *intensidad* de este **vector** ($\vec{V}$) es de 3 unidades.
> - La *dirección* de un **vector** ($\vec{V}$) es la misma *dirección* que la de la recta $AB$.
> - El *sentido* del **vector** ($\vec{V}$) es desde $A$ hasta $B$.

> [!note] Un vector se representa de las siguientes formas:
> $\vec{V}$: Expresa *magnitud* y *dirección*.
> $\begin{vmatrix}\vec{V}\end{vmatrix}$: Expresa el *módulo* sin *dirección*.

## VECTOR UNITARIO

Un **vector unitario** ($\vec{u}$) es el que su *módulo* vale una unidad.

Si un **vector** ($\vec{V}$) es paralelo a un **vector unitario** ($\vec{u}$) y del mismo *sentido*, se puede representar de la siguiente forma:

$$
\vec{V} = \begin{vmatrix}\vec{V}\end{vmatrix} \cdot \vec{u}
$$

> [!quote] Donde:
> - $\begin{vmatrix}\vec{V}\end{vmatrix}$: Representa el *módulo* del vector representado.
> - $\vec{u}$: Representa la *dirección* y *sentido*.

## SUMA DE VECTORES

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO

# \############################

## MAGNITUD

| CALCULAR MAGNITUD  |
|:------------------:|
| `sqrt(x^2 + y^2)` |

```python
import math

def calculate_dis(x: float, y: float) -> float:
    return math.sqrt((x ** 2) + (y ** 2))
```

|    CALCULAR MAGNITUD     |
|:------------------------:|
| `sqrt(x^2 + y^2 + z^2)` |

```python
import math

def calculate_dis(x: float, y: float, z: float) -> float:
    return math.sqrt((x ** 2) + (y ** 2) + (z ** 2))
```

## DIRECCIÓN

| CALCULAR DIRECCIÓN |
|:------------------:|
|   `atan(y / x)`   |

```python
import math

def calculate_dir(x: float, y: float) -> float:
    if x == 0:
        return math.pi * (0.5 if y > 0 else 1.5)
    else:
        return math.atan(y / x)
```

## TRANSFORMACIÓN

![dibujo_tranformacion_de_vectores](../excalidraw/dibujo_tranformacion_de_vectores.md)

## DOT PRODUCT

`Ax*Bx + Ay*By`

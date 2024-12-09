---
author: Mindusting
corrected: true
tags:
  - Programming/Python/Map
title: Map en Python
---

# CLASE MAP

La [clase](py_class.md) `map` para aplicar una [función](py_function.md) a todos los *elementos* de un *iterable*, guardando el resultado en un **objeto** de tipo `map`, pudiendo convertir este último en un nuevo *iterable*.

> [!abstract] SINTAXIS
> map(***\[function]***, ***\[iterator]***)

---

> [!example] Ejemplos
> En estos ejemplos se hace uso de las [funciones lambda](py_lambda.md).

```python
# Eleva al cubo.
cubed = lambda x: x ** 3

# Lista de números para elevar al cubo.
nums = [3, 2, 5, 7]

# Aplicación de la función a todos los números.
res = list(map(cubed, nums))

print(res)
# SALIDA:
# [27, 8, 125, 343]
```

```python
# Formula de Pitagoras.
def pitagoras(dx: float, dy: float) -> float:
    return (dx ** 2 + dy ** 2) ** 0.5

# Lista de vectores.
vectors = [
    (1, 1),
    (3, 2),
    (5, 7)
]

# Se usa una función lambda para
# separar los valores del vector.
distances = tuple(map(lambda v: pitagoras(*v), vectors))

# Imprimimos las tres distancias.
for i, dist in enumerate(distances):
    print(f"{i}) {dist:0.6}")
# SALIDA:
# 0) 1.41421
# 1) 3.60555
# 2) 8.60233
```

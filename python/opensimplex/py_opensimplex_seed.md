---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/OpenSimplex
title: Función seed del módolo OpenSimplex en Python
---

La [función](../py_function.md) `seed` requiere de un argumento de tipo [`int`](../variables/py_int.md), este será la semilla (*seed*) que se usará para hacer el *simplex noise*.

```py
import opensimplex as ops

ops.seed(64)

print(ops.get_seed())
# SALIDA:
# 64
```

En este ejemplo se hace uso de la [función](../py_function.md) [`get_seed`](py_opensimplex_get_seed.md) para poder ver que la semilla sí a cambiado.

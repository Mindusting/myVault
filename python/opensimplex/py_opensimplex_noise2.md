---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/OpenSimplex
title: Función noise2 del módolo OpenSimplex en Python
---

La [función](../py_function.md) `noise2` requiere de dos argumentos, estos pueden ser tanto de tipo [`int`](../variables/py_int.md) como [`float`](../variables/py_float.md) e indican las coordenadas del del valor que queremos del *simplex noise*.

```py
import opensimplex as ops

ops.seed(64)

print(ops.noise2(0.1, 0.8))
# SALIDA:
# -0.21570461975214264
```

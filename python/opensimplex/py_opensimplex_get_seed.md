---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/OpenSimplex
title: Función get_seed del módolo OpenSimplex en Python
---

La [función](../py_function.md) `get_seed` devuelve un valor de tipo [`int`](../variables/py_int.md) indicando la semilla (*seed*) del *simplex noise*, la semilla es el número que se utiliza para generar el ruido.

```py
import opensimplex as ops

print(ops.get_seed())
# SALIDA:
# 3
```

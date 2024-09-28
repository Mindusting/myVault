---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Module
  - Programming/Python/OpenSimplex
title: Función random_seed del módolo OpenSimplex en Python
---

La [función](../py_function.md) `random_seed` establece como semilla (*seed*) del *simplex noise* como un número de tipo [`int`](../variables/py_int.md) """aleatorio""", y lo pongo entre comillas ya que si vemos el código de esta [función](../py_function.md) podemos ver que el número lo saca de la [función](../py_function.md) [`time_ns`](../time/time_time_ns.md) del [módulo](../py_module.md) [`time`](../time/py_time.md).

```py
import opensimplex as ops

ops.random_seed()

print(ops.get_seed())
```

En este ejemplo se hace uso de la [función](../py_function.md) [`get_seed`](py_opensimplex_get_seed.md) para poder ver que la semilla sí a cambiado.

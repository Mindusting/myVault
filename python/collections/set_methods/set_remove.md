---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Los B-Tree en Python
---

Si queremos que borrar un elemento del set y queremos que al intentar borrarlo, en caso de que no exista ese elemento [lanzaría una excepción](../../exceptions/Exceptions_Raise.md), se hace con el [método](../../classes/py_method.md) `remove`:

```py
my_set: set = {"Manzana", "Naranja", "Platano"}
my_set.remove("Platano")

print(my_set)
# SALIDA:
# {'Naranja', 'Manzana'}
```

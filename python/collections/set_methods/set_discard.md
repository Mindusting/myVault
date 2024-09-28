---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Los B-Tree en Python
---

Para borra un elemento del set sin que [lance una excepción](../../exceptions/Exceptions_Raise.md) en el caso de que este elemento no exista, se usa el [método](../../classes/py_method.md) `discard`:

```py
my_set: set = {"Manzana", "Naranja", "Platano"}
my_set.discard("Platano")

print(my_set)
# SALIDA:
# {'Manzana', 'Naranja'}
```

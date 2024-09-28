---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Los B-Tree en Python
---

El [método](../../classes/py_method.md) `intersection_update` es una combinación entre los [método](../../classes/py_method.md) [`update`](set_update.md) e [`intersection`](set_intersection.md) modificando el primer set, haciendo que solo tenga los elementos qué coincidan en el segundo set.

```py
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Naranja", "Manzana"}

set_1.intersection_update(set_2)

print(set_1)
# SALIDA:
# {'Naranja', 'Manzana'}
```

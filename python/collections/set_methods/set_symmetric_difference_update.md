---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Los B-Tree en Python
---

El [método](../../classes/py_method.md) `symmetric_difference_update` es una combinación entre los [método](../../classes/py_method.md) [`update`](set_update.md) e [`symmetric_difference`](set_symmetric_difference.md) modificando el primer set, haciendo que tenga los elementos de los dos set que no coincidieran en los dos:

```py
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Naranja", "Manzana"}

set_1.symmetric_difference_update(set_2)

print(set_1)
# SALIDA:
# {'Pera', 'Platano'}
```

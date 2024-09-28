---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Los B-Tree en Python
---

Para añadir un elemento nuevo a un ser se usa el [método](../../classes/py_method.md) `add`:

```py
my_set: set = {"Manzana", "Naranja", "Platano"}
my_set.add("Pera")

print(my_set)
# SALIDA:
# {'Manzana', 'Pera', 'Naranja', 'Platano'}
```

En caso de que el elemento ya exista dentro del set, teste no sufrirá ningún cambio.
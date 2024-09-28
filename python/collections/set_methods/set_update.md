---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Los B-Tree en Python
---

Para añadir múltiples elementos a un set se usa el [método](../../classes/py_method.md) `update`:

```py
my_set: set = {"Manzana", "Naranja", "Platano"}
my_set.update({"Pera", "Arándano", "Berengena"})

print(my_set)
# SALIDA:
# {'Naranja', 'Manzana', 'Pera', 'Berengena', 'Arándano', 'Platano'}
```

>[!note]
>En este caso se añade los elementos de un set al otro, pero, también hay que tener en cuenta que también funciona con una [lista](../py_list.md), una [tupla](../Collections_tuple.md) o con un [string](../../variables/py_str.md) (En este caso lo que haría sería guardar en el set todos los caracteres que tenga).

---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Los B-Tree en Python
---

El [método](../../classes/py_method.md) `union` funciona de forma similar al [`update`](set_update.md), con la diferencia que este no cambia ninguno de los dos sets, si no qué devuelve un nuevo set cono todos los elementos de los sets unidos.

```py
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Arándano", "Berengena"}

print(set_1.union(set_2))
# SALIDA:
# {'Pera', 'Platano', 'Arándano', 'Berengena', 'Manzana', 'Naranja'}
```

>[!note]
>Al igual que con el [método](../../classes/py_method.md) [`update`](set_update.md), es posible sustituir el `set_2` por una [lista](../py_list.md), una [tupla](../Collections_tuple.md) o un [string](../../variables/py_str.md).

---

Otra forma de hacer esto mismo es a trabes de una sintaxis más simple haciendo uso del carácter `|`:

```py
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Arándano", "Berengena"}

print(set_1 | set_2)
# SALIDA:
# {'Pera', 'Platano', 'Arándano', 'Berengena', 'Manzana', 'Naranja'}
```

>[!warning]
>Esta forma reducida solo soporta set con set.

---

En cualquiera de estas dos opciones se puede especificar más set a combinar:

```py
set_1: set = {"Manzana", "Naranja"}
set_2: set = {"Platano", "Pera"}
set_3: set = {"Arándano", "Berengena"}

print(set_1.union(set_2, set_3))
print(set_1 | set_2 | set_3)
# SALIDA:
# {'Berengena', 'Naranja', 'Manzana', 'Arándano', 'Pera', 'Platano'}
# {'Berengena', 'Naranja', 'Manzana', 'Arándano', 'Pera', 'Platano'}
```

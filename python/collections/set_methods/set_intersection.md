---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Los B-Tree en Python
---

El [método](../../classes/py_method.md) `intersection` funciona de forma similar al [`union`](set_union.md), con la diferencia que este devuelve un set con los elementos que coincidan en los dos sets.

```py
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Naranja", "Manzana"}

print(set_1.intersection(set_2))
# SALIDA:
# {'Naranja', 'Manzana'}
```

>[!note]
>Al igual que con el [método](../../classes/py_method.md) [`union`](set_union.md), es posible sustituir el `set_2` por una [lista](../py_list.md), una [tupla](../Collections_tuple.md) o un [string](../../variables/py_str.md).

---

Otra forma de hacer esto mismo es a trabes de una sintaxis más simple haciendo uso del carácter `&`:

```py
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Naranja", "Manzana"}

print(set_1 & set_2)
# SALIDA:
# {'Naranja', 'Manzana'}
```

>[!warning]
>Esta forma reducida solo soporta set con set.

---

En cualquiera de estas dos opciones se puede especificar más set a combinar:

```py
set_1: set = {"Manzana", "Naranja"}
set_2: set = {"Naranja", "Manzana"}
set_3: set = {"Manzana", "Platano"}

print(set_1.intersection(set_2, set_3))
print(set_1 & set_2 & set_3)
# SALIDA:
# {'Manzana'}
# {'Manzana'}
```

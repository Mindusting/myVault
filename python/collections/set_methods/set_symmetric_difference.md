---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Los B-Tree en Python
---

[set_difference](set_difference.md)

El [método](../../classes/py_method.md) `symmetric_difference` es similar al [método](../../classes/py_method.md) [difference](set_difference.md), con la diferencia que este devuelve un set con los elementos que no coincidan en ambos sets:

```py
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Naranja", "Manzana"}

print(set_1.symmetric_difference(set_2))
# SALIDA:
# {'Pera', 'Platano'}
```

>[!note]
>Al igual que con el [método](../../classes/py_method.md) [`union`](set_union.md), es posible sustituir el `set_2` por una [lista](../py_list.md), una [tupla](../Collections_tuple.md) o un [string](../../variables/py_str.md).

---

Otra forma de hacer esto mismo es a trabes de una sintaxis más simple haciendo uso del carácter `^`:

```py
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Naranja", "Manzana"}

print(set_1 ^ set_2)
# SALIDA:
# {'Pera', 'Platano'}
```

>[!warning]
>Esta forma reducida solo soporta set con set.

---

Si queremos hacer este proceso con múltiples sets simultáneamente, estaremos obligados a utilizar la versión corta, ya que el [método](../../classes/py_method.md) solo soporta un argumento:

```py
set_1: set = {"Manzana", "Naranja"}
set_2: set = {"Naranja", "Manzana"}
set_3: set = {"Manzana", "Platano"}

print(set_1 ^ set_2 ^ set_3)
# SALIDA:
# {'Platano', 'Manzana'}
```

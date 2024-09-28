---
author: Mindusting
corrected: false
tags:
  - Programming/Python
title: Los B-Tree en Python
---

El [método](../../classes/py_method.md) `difference` devuelve un set con los elementos del primer set que no estén en el segundo:

```py
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Naranja", "Manzana"}

print(set_1.difference(set_2))
# SALIDA:
# {'Platano'}
```

>[!note]
>Al igual que con el [método](../../classes/py_method.md) [`union`](set_union.md), es posible sustituir el `set_2` por una [lista](../py_list.md), una [tupla](../Collections_tuple.md) o un [string](../../variables/py_str.md).

---

Otra forma de hacer esto mismo es a trabes de una sintaxis más simple haciendo uso del carácter `-`:

```py
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Naranja", "Manzana"}

print(set_1 - set_2)
# SALIDA:
# {'Platano'}
```

>[!warning]
>Esta forma reducida solo soporta set con set.

---

En cualquiera de estas dos opciones se puede especificar más set a combinar:

```py
set_1: set = {"Manzana", "Naranja"}
set_2: set = {"Pera", "Manzana"}
set_3: set = {"Manzana", "Platano"}

print(set_1.difference(set_2, set_3))
print(set_1 - set_2 - set_3)
# SALIDA:
# {'Naranja'}
# {'Naranja'}
```

---
author: Mindusting
corrected: false
tags:
  - Programming/Python/Set
title: Los conjuntos en Python
---

<h1 style="text-align:center;">SETS EN PYTHON</h1>

---

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

# REFERENCIAS WEB

- [WEB - W3 (set)](https://www.w3schools.com/python/python_sets.asp)
- [WEB - W3 (methods)](https://www.w3schools.com/python/python_sets_methods.asp)

# SET

- [¿Qué es un set o B-Tree en programación?](../../pc/pc_btree.md)

Para declarar un [**set**](../../pc/pc_btree.md) en Python se puede hacer de las siguientes formas:

```py
set1 = {}
set2 = set()

set3: set = {}
set4: set = set()
```

Con la [clase](../py_class.md) `set` se puede transformar por ejemplo una [lista](py_list.md) en un set:

```py
my_list: list = ["a", "a", "b", "c"]

my_set: set = set(my_list)

print(my_set)
# SALIDA:
# {'b', 'c', 'a'}
```

>[!info] INFO
>Los elemento que se encuentren dentro del set no tienen por qué estar ordenados.

Como los set no pueden almacenar varias veces el mismo valor, al haber dos `"a"` dentro de la lista, en el set solo hay una, esto mismo se aplica a los valores `True` con el `1` y el `False` con el `0`.

```py
my_list: list = [True, 1, False, 0]

my_set: set = set(my_list)

print(my_set)
# SALIDA:
# {False, True}
```

# MÉTODOS

> [!todo] TODO:
> - [ ] Copiar todo el contenido de los métodos del set y ponerlos aquí.

- [AÑADIR UN ELEMENTO](set_methods/set_add.md)
- [AÑADIR MULTIPLES ELEMENTOS](set_methods/set_update.md)
- BORRAR ELEMENTOS
    - [BORRAR CON EXCEPCIÓN](set_methods/set_remove.md)
    - [BORRAR SIN EXCEPCIÓN](set_methods/set_discard.md)
    - [BORRAR ÚLTIMO ELEMENTO](set_methods/set_pop.md)
    - [BORRAR TODOS LOS ELEMENTOS](set_methods/set_clear.md)
- [UNIR ELEMENTOS](set_methods/set_union.md)
- [INTERSECCIÓN DE ELEMENTOS](set_methods/set_intersection.md)
    - [AÑADIR INTERSECCIÓN DE ELEMENTOS](set_methods/set_intersection_Update.md)
- [DIFERECIA DE ELEMENTOS](set_methods/set_difference.md)
    - [AÑADIR DIFERENCIA ENTRE ELEMENTOS](set_methods/set_differece_update.md)
- [DIFERENCIA SIMETRICA DE ELEMENTOS](set_methods/set_symmetric_difference.md)
    - [AÑADIR DIFERENCIA SIMETRICA DE ELEMENTOS](set_methods/set_symmetric_difference_update.md)

# BUCLES

Se puede usar el set en un [bucle for](../loops/py_for.md) al estilo de [for-each](../loops/py_for_each.md):

```py
my_set: set = {"Manzana", "Naranja", "Platano"}

print(my_set)

for element in my_set:
    print(element)
# SALIDA:
# {'Naranja', 'Manzana', 'Platano'}
# Naranja
# Manzana
# Platano
```

>[!note] NOTE
>Nota que el orden en el qué se han iterado los elementos en el bucle, es el mismo que el orden en el que estaban en el set.

# EXISTENCIA DE ELEMENTO

Para poder saber si existe un elemento en concreto dentro del set se usa la palabra clave `in`:

```py
my_set: set = {"Manzana", "Naranja", "Platano"}

print("Platano" in my_set)
# SALIDA:
# True
```

Como se puede ver este nos devolverá un valor [booleano](../variables/py_bool.md) indicando si existe o no dentro del set.

# VARIABLE INMUTABLE

Existe una variante del set la cual es inmutable, esto quiere decir que una vez es declarado, no se puede cambiar, para ello se usa la [clase](../py_class.md) `frozenset` (Set congelado):

```py
my_set: set = {"Manzana", "Naranja", "Platano"}
my_frozenset: frozenset = frozenset(my_set)

print(my_frozenset)
# SALIDA:
# frozenset({'Platano', 'Naranja', 'Manzana'})
```

Este tipo de set funcionará igual que un set normal, con la diferencia que si intentamos modificarlo ocurrirá un error, ya que está pesado para que no sea modificado, se podría decir que es la versión [`contant`](../../pc/pc_constant.md) del set.

# MÉTODOS

add
clear
copy
difference
difference_update
discard
intersection
intersection_update
isdisjoint
issubset
issuperset
pop
remove
symmetric_difference
symmetric_difference_update
union
update

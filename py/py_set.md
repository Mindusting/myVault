---
author: Mindusting
corrected: false
tags:
  - Programming/Python/DataStructure
title: Los conjuntos en Python
---

# SET

> [!help] REFERENCIAS WEB
> - [W3 (set)](https://www.w3schools.com/python/python_sets.asp)
> - [W3 (set methods)](https://www.w3schools.com/python/python_sets_methods.asp)

- [¿Qué es un set o B-Tree en programación?](../../pc/pc_btree.md)

Para declarar un [**set**](../../pc/pc_btree.md) en Python se puede hacer de las siguientes formas:

```python
set1 = {}
set2 = set()

set3: set = {}
set4: set = set()
```

Con la [clase](py_class.md) `set` se puede transformar por ejemplo una [lista](py_list.md) en un set:

```python
my_list: list = ["a", "a", "b", "c"]

my_set: set = set(my_list)

print(my_set)
# SALIDA:
# {'b', 'c', 'a'}
```

> [!info] INFO
> Los elemento que se encuentren dentro del set no tienen por qué estar ordenados.

Como los set no pueden almacenar varias veces el mismo valor, al haber dos `"a"` dentro de la lista, en el set solo hay una, esto mismo se aplica a los valores `True` con el `1` y el `False` con el `0`.

```python
my_list: list = [True, 1, False, 0]

my_set: set = set(my_list)

print(my_set)
# SALIDA:
# {False, True}
```

## MÉTODOS

> [!todo] TODO:
> - [ ] Copiar todo el contenido de los métodos del set y ponerlos aquí.

### SET

Para añadir un elemento nuevo a un ser se usa el [método](classes/py_method.md) `add`:

```python
my_set: set = {"Manzana", "Naranja", "Platano"}
my_set.add("Pera")

print(my_set)
# SALIDA:
# {'Manzana', 'Pera', 'Naranja', 'Platano'}
```

En caso de que el elemento ya exista dentro del set, teste no sufrirá ningún cambio.

### UPDATE

Para añadir múltiples elementos a un set se usa el [método](classes/py_method.md) `update`:

```python
my_set: set = {"Manzana", "Naranja", "Platano"}
my_set.update({"Pera", "Arándano", "Berengena"})

print(my_set)
# SALIDA:
# {'Naranja', 'Manzana', 'Pera', 'Berengena', 'Arándano', 'Platano'}
```

> [!note]
> En este caso se añade los elementos de un set al otro, pero, también hay que tener en cuenta que también funciona con una [lista](py_list.md), una [tupla](py_tuple.md) o con un [string](variables/py_str.md) (En este caso lo que haría sería guardar en el set todos los caracteres que tenga).

### REMOVE

Si queremos que borrar un elemento del set y queremos que al intentar borrarlo, en caso de que no exista ese elemento [lanzaría una excepción](exceptions/Exceptions_Raise.md), se hace con el [método](classes/py_method.md) `remove`:

```python
my_set: set = {"Manzana", "Naranja", "Platano"}
my_set.remove("Platano")

print(my_set)
# SALIDA:
# {'Naranja', 'Manzana'}
```

### DISCARD

Para borra un elemento del set sin que [lance una excepción](exceptions/Exceptions_Raise.md) en el caso de que este elemento no exista, se usa el [método](classes/py_method.md) `discard`:

```python
my_set: set = {"Manzana", "Naranja", "Platano"}
my_set.discard("Platano")

print(my_set)
# SALIDA:
# {'Manzana', 'Naranja'}
```

### POP

En el caso de qué queramos borrar el último elemento del set se puede usar el [método](classes/py_method.md) `pop`, este también devuelve el último valor, por lo que, como se puede ver en el ejemplo, se puede guardar el valor guardado:

```python
my_set: set = {"Manzana", "Naranja", "Platano"}
last_element: str = my_set.pop()

print(my_set)
print(last_element)
# SALIDA:
# {'Naranja', 'Manzana'}
# Platano
```

> [!warning]
> Cuidado con este [método](classes/py_method.md), como el contenido del set no tiene por qué estar ordenado siempre de la misma forma, el resultado de este ejemplo puede cambiar cada vez que se ejecute.

### CLEAR

Para borrar todos los elementos del set se puede usar el [método](classes/py_method.md) `clear`:

```python
my_set: set = {"Manzana", "Naranja", "Platano"}
my_set.clear()

print(my_set)
# SALIDA:
# set()
```

### UNION

El [método](classes/py_method.md) `union` funciona de forma similar al [`update`](#UPDATE), con la diferencia que este no cambia ninguno de los dos sets, si no qué devuelve un nuevo set cono todos los elementos de los sets unidos.

```python
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Arándano", "Berengena"}

print(set_1.union(set_2))
# SALIDA:
# {'Pera', 'Platano', 'Arándano', 'Berengena', 'Manzana', 'Naranja'}
```

> [!note]
> Al igual que con el [método](classes/py_method.md) [`update`](#UPDATE), es posible sustituir el `set_2` por una [lista](py_list.md), una [tupla](py_tuple.md) o un [string](variables/py_str.md).

---

Otra forma de hacer esto mismo es a trabes de una sintaxis más simple haciendo uso del carácter `|`:

```python
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Arándano", "Berengena"}

print(set_1 | set_2)
# SALIDA:
# {'Pera', 'Platano', 'Arándano', 'Berengena', 'Manzana', 'Naranja'}
```

> [!warning]
> Esta forma reducida solo soporta set con set.

---

En cualquiera de estas dos opciones se puede especificar más set a combinar:

```python
set_1: set = {"Manzana", "Naranja"}
set_2: set = {"Platano", "Pera"}
set_3: set = {"Arándano", "Berengena"}

print(set_1.union(set_2, set_3))
print(set_1 | set_2 | set_3)
# SALIDA:
# {'Berengena', 'Naranja', 'Manzana', 'Arándano', 'Pera', 'Platano'}
# {'Berengena', 'Naranja', 'Manzana', 'Arándano', 'Pera', 'Platano'}
```

### INTERSECTION

El [método](classes/py_method.md) `intersection` funciona de forma similar al [`union`](#UNION), con la diferencia que este devuelve un set con los elementos que coincidan en los dos sets.

```python
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Naranja", "Manzana"}

print(set_1.intersection(set_2))
# SALIDA:
# {'Naranja', 'Manzana'}
```

> [!note]
> Al igual que con el [método](classes/py_method.md) [`union`](#UNION), es posible sustituir el `set_2` por una [lista](py_list.md), una [tupla](py_tuple.md) o un [string](variables/py_str.md).

---

Otra forma de hacer esto mismo es a trabes de una sintaxis más simple haciendo uso del carácter `&`:

```python
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Naranja", "Manzana"}

print(set_1 & set_2)
# SALIDA:
# {'Naranja', 'Manzana'}
```

> [!warning]
> Esta forma reducida solo soporta set con set.

---

En cualquiera de estas dos opciones se puede especificar más set a combinar:

```python
set_1: set = {"Manzana", "Naranja"}
set_2: set = {"Naranja", "Manzana"}
set_3: set = {"Manzana", "Platano"}

print(set_1.intersection(set_2, set_3))
print(set_1 & set_2 & set_3)
# SALIDA:
# {'Manzana'}
# {'Manzana'}
```

### INTERSECTION UPDATE

El [método](classes/py_method.md) `intersection_update` es una combinación entre los [método](classes/py_method.md) [`update`](#UPDATE) e [`intersection`](#INTERSECTION) modificando el primer set, haciendo que solo tenga los elementos qué coincidan en el segundo set.

```python
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Naranja", "Manzana"}

set_1.intersection_update(set_2)

print(set_1)
# SALIDA:
# {'Naranja', 'Manzana'}
```

### DIFFERENCE

El [método](classes/py_method.md) `difference` devuelve un set con los elementos del primer set que no estén en el segundo:

```python
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Naranja", "Manzana"}

print(set_1.difference(set_2))
# SALIDA:
# {'Platano'}
```

> [!note]
> Al igual que con el [método](classes/py_method.md) [`union`](#UNION), es posible sustituir el `set_2` por una [lista](py_list.md), una [tupla](py_tuple.md) o un [string](variables/py_str.md).

---

Otra forma de hacer esto mismo es a trabes de una sintaxis más simple haciendo uso del carácter `-`:

```python
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Naranja", "Manzana"}

print(set_1 - set_2)
# SALIDA:
# {'Platano'}
```

> [!warning]
> Esta forma reducida solo soporta set con set.

---

En cualquiera de estas dos opciones se puede especificar más set a combinar:

```python
set_1: set = {"Manzana", "Naranja"}
set_2: set = {"Pera", "Manzana"}
set_3: set = {"Manzana", "Platano"}

print(set_1.difference(set_2, set_3))
print(set_1 - set_2 - set_3)
# SALIDA:
# {'Naranja'}
# {'Naranja'}
```

### DIFFERENCE UPDATE

El [método](classes/py_method.md) `difference_update` es una combinación entre los [método](classes/py_method.md) [`update`](#UPDATE) e [`difference`](#DIFFERENCE) modificando el primer set, haciendo que solo tenga los elementos qué coincidan en el segundo set.

```python
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Naranja", "Manzana"}

set_1.difference_update(set_2)

print(set_1)
# SALIDA:
# {'Platano'}
```

### SYMMETRIC DIFFERENCE

El [método](classes/py_method.md) `symmetric_difference` es similar al [método](classes/py_method.md) [difference](#DIFFERENCE), con la diferencia que este devuelve un set con los elementos que no coincidan en ambos sets:

```python
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Naranja", "Manzana"}

print(set_1.symmetric_difference(set_2))
# SALIDA:
# {'Pera', 'Platano'}
```

> [!note]
> Al igual que con el [método](classes/py_method.md) [`union`](#UNION), es posible sustituir el `set_2` por una [lista](py_list.md), una [tupla](py_tuple.md) o un [string](variables/py_str.md).

---

Otra forma de hacer esto mismo es a trabes de una sintaxis más simple haciendo uso del carácter `^`:

```python
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Naranja", "Manzana"}

print(set_1 ^ set_2)
# SALIDA:
# {'Pera', 'Platano'}
```

> [!warning]
> Esta forma reducida solo soporta set con set.

---

Si queremos hacer este proceso con múltiples sets simultáneamente, estaremos obligados a utilizar la versión corta, ya que el [método](classes/py_method.md) solo soporta un argumento:

```python
set_1: set = {"Manzana", "Naranja"}
set_2: set = {"Naranja", "Manzana"}
set_3: set = {"Manzana", "Platano"}

print(set_1 ^ set_2 ^ set_3)
# SALIDA:
# {'Platano', 'Manzana'}
```

### SYMMETRIC DIFERENCE UPDATE

El [método](classes/py_method.md) `symmetric_difference_update` es una combinación entre los [método](classes/py_method.md) [`update`](#UPDATE) e [`symmetric_difference`](#SYMMETRIC%20DIFFERENCE) modificando el primer set, haciendo que tenga los elementos de los dos set que no coincidieran en los dos:

```python
set_1: set = {"Manzana", "Naranja", "Platano"}
set_2: set = {"Pera", "Naranja", "Manzana"}

set_1.symmetric_difference_update(set_2)

print(set_1)
# SALIDA:
# {'Pera', 'Platano'}
```

## BUCLES

Se puede usar el set en un [bucle for](loops/py_for.md) al estilo de [for-each](loops/py_for_each.md):

```python
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

> [!note] NOTE
> Nota que el orden en el qué se han iterado los elementos en el bucle, es el mismo que el orden en el que estaban en el set.

## EXISTENCIA DE ELEMENTO

Para poder saber si existe un elemento en concreto dentro del set se usa la palabra clave `in`:

```python
my_set: set = {"Manzana", "Naranja", "Platano"}

print("Platano" in my_set)
# SALIDA:
# True
```

Como se puede ver este nos devolverá un valor [booleano](variables/py_bool.md) indicando si existe o no dentro del set.

## VARIABLE INMUTABLE

Existe una variante del set la cual es inmutable, esto quiere decir que una vez es declarado, no se puede cambiar, para ello se usa la [clase](py_class.md) `frozenset` (Set congelado):

```python
my_set: set = {"Manzana", "Naranja", "Platano"}
my_frozenset: frozenset = frozenset(my_set)

print(my_frozenset)
# SALIDA:
# frozenset({'Platano', 'Naranja', 'Manzana'})
```

Este tipo de set funcionará igual que un set normal, con la diferencia que si intentamos modificarlo ocurrirá un error, ya que está pesado para que no sea modificado, se podría decir que es la versión [`contant`](../../pc/pc_constant.md) del set.

%%
## MÉTODOS

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
%%

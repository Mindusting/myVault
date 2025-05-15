---
author: Mindusting
corrected: false
tags:
  - Programming/Python/DataStructure
title: Diccionarios en Python
---

# DICCIONARIOS

> [!help]- REFERENCIAS WEB
> - [W3 (dict)](https://www.w3schools.com/python/python_dictionaries.asp)
> - [W3 (dict methods)](https://www.w3schools.com/python/python_ref_dictionary.asp)

> [!faq]- FAQ
> - [¿Qué es un diccionario en programación?](../pc/pc_dictionary.md)

Los **diccionarios** son similares a las [listas](py_list.md) con la diferencias que estos en vez de tener un *índice* asociado a cada *valor*, tiene una *valor* llamado `key` asociado a cada `value` y cada par de estos se llama `item`.

> [!info] INFO
> - Cabe resaltar que las `key` no se pueden repetir ya que es lo que se utiliza para referenciar los valores guardados, si intentamos guardar otro valor con la misma `key` simplemente se sobrescribirá.
> <br>
> - Otro apunte es que se puede usar cualquier cosa tanto como `key` como `value`, esto pueden ser [`int`](py_int.md), [`float`](py_float.md), [`string`](py_str.md), [`objetos`](py_class.md)... cualquier cosa.

Para crear un **diccionario** vacío podemos hacerlo de las siguientes formas:

```python
dict1 = dict()
dict2: dict = dict()
```

Si queremos crear un **diccionario** que tenga ya *items* tendremos podemos hacerlo de la siguiente forma:

```python
dict1 = {"pi": 3.1415926535}
dict2: dict = {"pi": 3.1415926535}
```

Se utilizan las *llaves* al igual que con los [`set`](py_set.md), con la diferencia que en este caso la `key` (*siendo en este caso `pi`*) y el `value` (*siendo en este caso `3.1415926535`*) separados por **dos puntos** (`:`).

## AGREGAR INFORMACIÓN

Para insertar información dentro de un **diccionario** podemos hacerlo de la siguiente forma:

```python
x: dict = dict()

x["name"] = "Adelio"
x["age"]  = 18

print(x)
# SALIDA:
# {'name': 'Adelio', 'age': 18}
```

## MODIFICAR INFORMACIÓN

Para modificar información de un **diccionario** se hace de la misma forma que el agregar información, pero tendremos que hacer referencia a una `key` que ya exista dentro del **diccionario**:

```python
x: dict = {"name": "Adelio", "age": 18}

x["name"] = "Adelia"
x["age"]  = 20

print(x)
# SALIDA:
# {'name': 'Adelia', 'age": 20}
```

## OBTENER INFORMACIÓN

Para acceder a la información del **diccionario** tendremos que conocer la `key` del `value` que queremos consultar:

```python
x: dict = {"name": "Adelia", "age": 20}

print(x["name"])
print(x["age"])
# SALIDA:
# Adelia
# 20
```

## BORRAR INFORMACIÓN

Para borrar información del **diccionario** tendremos que conocer la `key` del `item` que queremos borrar:

```python
x: dict = {"name": "Adelia", "age": 20}

del x["name"]

print(x)
# SALIDA:
# {'age': 20}
```

# MÉTODOS

- `clear`: Bacía el diccionario.
- `copy`: Crea una copia del diccionario.
- `fromkeys`: Crea un diccionario con las `key` indicadas en un iterable y le asigna el valor indicado a todas las `key`.
- `get`: El primer argumento es la `key`, si ésta no existe, devuelve el `default` indicado.
- `items`: Devuelve un objeto de tipo `dict_items`, este se puede convertir en una lista.
- `keys`: Devuelve un objeto de tipo `dict_keys`, este puede ser transformado en una lista con las `key` del diccionario.
- `pop`: Elimina el `item` con la `key` indicada y devuelve su valor, si no existe el `item` devuelve el `defaul` indicado.
- `popitem`: Devuelve y elimina el último `item` del diccionario.
- `setdefault`: Devuelve el `value` de la `key` indicada, si esta no existe crea un nuevo `item` con la `key` y el `value` indicado y devuelve el `value` indicado.
- `update`: Añade el diccionario indicado.
- `values`: Devuelve un objeto de tipo `dict_values`, este puede ser transformado en una lista con los `value` del diccionario.

---
author: Mindusting
corrected: true
tags:
  - Programming/Python/Module
  - Programming/Python/OS/Path
title: Módulo OS en Python
rating: 0.75
---

# PATH EN PYTHON

> [!help]- REFERENCIAS WEB
> - [Python Doc (os.path)](https://docs.python.org/3/library/os.path.html)
> - [geeksforgeeks](https://www.geeksforgeeks.org/os-path-module-python/)

El módulo `path` es en sí un submódulo del [módulo `os`](../py_os.md); este permite trabajar sobre **rutas**.

## EXISTENCIA DE RUTA

Para comprobar la existencia de una **ruta** se usa la [función](../../py_func.md) `exists`; este recibe la **ruta** a evaluar a través de un [`str`](../../py_str.md) o [`bytes`](../../py_bytes.md); esta nos indicará si la **ruta** existe mediante un valor [`bool`](../../py_bool.md), siendo `True` en caso de que exista, de lo contrario `False`.

> [!abstract] SINTAXIS
> exists(***\[path\]***)

```python
import os

path: str = "./my_file.txt"

print(os.path.exists(path))
# SALIDA:
# True
```

## TIPO DE RUTA

Las **rutas** se pueden dividir en tres tipos: *archivo*, *directorio* y *link*; para poder saber en qué combinación de estos tipos pertenece la **ruta** sobre la que estamos trabajando, se usan las siguientes tres [funciones](../../py_func.md):

- `islink`: indica si es un enlace.
- `isfile`: indica si es un archivo (*o hace referencia a uno*).
- `isdir`: indica si es un directorio (*o hace referencia a uno*).

> [!note] NOTA
> La matización "*o hace referencia a uno*" se refiere a que si la **ruta** que le pasamos como argumento es un link, dependiendo de si hace referencia a un archivo o directorio, esta [función](../../py_func.md) también nos puede dar el valor `True`; justo debajo tienes una [tabla de resultados](#^type-table) por si quieres consultarla.

| TYPE      | IS LINK | IS FILE | IS DIR  |
|:--------- |:------- |:------- |:------- |
| File      | `False` | `True`  | `False` |
| Dir       | `False` | `False` | `True`  |
| File link | `True`  | `True`  | `False` |
| Dir link  | `True`  | `False` | `True`  |
^type-table

## TROCEAR LA RUTA

Para separar el último **elemento** de una **ruta** del resto de la ruta podemos usar la [función](../../py_func.md) `basename`; por otro lado si lo que queremos es lo contrario, quedarnos con la **ruta** sin el último **elemento** podemos usar `dirname`; estas dos [funciones](../../py_func.md) reciben un la **ruta** como parámetro y devuelven el resultado.

A continuación veremos una porción de código junto a una tabla que nos permitirá entender mejor cómo es que funcionan estas [funciones](../../py_func.md):

```python
import os

path: str = ""

print(os.path.basename(path))
print(os.path.dirname(path))
```

En esta tabla podemos ver los valores que se ofrecen a las [funciones](../../py_func.md) y cual es el valor que devuelve cada una.

| PATH                 | BASE       | DIR         |
|:-------------------- |:---------- |:----------- |
| `dir1/dir2/file.txt` | `file.txt` | `dir1/dir2` |
| `dir1/dir2/`         |            | `dir1/dir2` |
| `dir1/dir2`          | `dir2`     | `dir1`      |

## NORMALIZACIÓN DE RUTA

La normalización de la **ruta** permite limpiarlas y adecuarlas para el sistema operativo en el que se esté ejecutando el programa; para ello tenemos dos [funciones](../../py_func.md):

- `normcase`: en Linux y Mac OS no hace nada, pero en Windows pone todo el texto en minúsculas y sustituye las barras (`/`) por constrabarras (`\`).
- `normpath`: quita las referencias a la propia carpeta (`./`); por ejemplo `/dir1/./dir2` lo convierte en `/dir1/dir2`.

## RUTA ABSOLUTA

Para saber si una ruta es absoluta se usa la [función](../../py_func.md) `isabs`, este recibe la ruta como argumento y devuelve un valor [`bool`](../../py_bool.md).

```python
import os

print(os.path.isabs("/bin"))
print(os.path.isabs("code"))
# SALIDA:
# True
# False
```
